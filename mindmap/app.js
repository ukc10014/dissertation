const svg = document.getElementById("map");
const NS = "http://www.w3.org/2000/svg";

const focusTitle = document.getElementById("focus-title");
const focusMeta = document.getElementById("focus-meta");
const childrenList = document.getElementById("children-list");
const sourcesList = document.getElementById("sources-list");
const breadcrumb = document.getElementById("breadcrumb");

const homeBtn = document.getElementById("home-btn");
const upBtn = document.getElementById("up-btn");
const hierarchyBtn = document.getElementById("mode-hierarchy-btn");
const flatBtn = document.getElementById("mode-flat-btn");
const flatFilters = document.getElementById("flat-filters");

const HIERARCHY_VIEW = { width: 1200, height: 760 };
const FLAT_VIEW = { width: 1600, height: 1200 };
const TYPE_RING = {
  root: 0.02,
  document: 0.24,
  section: 0.43,
  source: 0.61,
};

const colors = {
  root: getCssVar("--root"),
  document: getCssVar("--document"),
  section: getCssVar("--section"),
  source: getCssVar("--source"),
};

const flatState = {
  positions: new Map(),
  velocities: new Map(),
  radii: new Map(),
  nodeVisuals: new Map(),
  edgeVisuals: [],
  hoveredId: null,
  focusId: null,
  animationFrame: 0,
  alpha: 0,
  renderEdges: null,
  nodesById: new Map(),
  visibleIds: [],
  draggedId: null,
};

function getCssVar(name) {
  return getComputedStyle(document.documentElement).getPropertyValue(name).trim();
}

function clear(el) {
  while (el.firstChild) el.removeChild(el.firstChild);
}

function shortLabel(label, max = 36) {
  return label.length <= max ? label : `${label.slice(0, max - 1)}…`;
}

function polar(cx, cy, r, idx, total) {
  const angle = -Math.PI / 2 + (idx / Math.max(total, 1)) * Math.PI * 2;
  return { x: cx + r * Math.cos(angle), y: cy + r * Math.sin(angle) };
}

function hash01(input) {
  let hash = 2166136261;
  for (let i = 0; i < input.length; i += 1) {
    hash ^= input.charCodeAt(i);
    hash = Math.imul(hash, 16777619);
  }
  return (hash >>> 0) / 4294967295;
}

function clamp(value, min, max) {
  return Math.min(max, Math.max(min, value));
}

function setViewBox(view) {
  svg.setAttribute("viewBox", `0 0 ${view.width} ${view.height}`);
}

async function loadGraph() {
  const res = await fetch("./argument_graph.json");
  if (!res.ok) throw new Error(`Failed to load graph: ${res.status}`);
  return res.json();
}

function graphIndex(graph) {
  const nodesById = new Map(graph.nodes.map((n) => [n.id, n]));
  const outgoing = new Map();
  const incoming = new Map();

  for (const edge of graph.edges) {
    if (!outgoing.has(edge.source)) outgoing.set(edge.source, []);
    if (!incoming.has(edge.target)) incoming.set(edge.target, []);
    outgoing.get(edge.source).push(edge);
    incoming.get(edge.target).push(edge);
  }

  return { nodesById, outgoing, incoming, edges: graph.edges, nodes: graph.nodes };
}

function parentOf(id, idx) {
  const inEdges = idx.incoming.get(id) || [];
  const containsParent = inEdges.find((e) => e.type === "contains");
  return containsParent ? containsParent.source : null;
}

function childrenOf(id, idx) {
  const out = idx.outgoing.get(id) || [];
  return out.filter((e) => e.type === "contains").map((e) => idx.nodesById.get(e.target));
}

function sourcesOf(id, idx) {
  const out = idx.outgoing.get(id) || [];
  return out.filter((e) => e.type === "cites").map((e) => idx.nodesById.get(e.target));
}

function lineage(id, idx) {
  const chain = [];
  let cursor = id;
  while (cursor) {
    chain.push(idx.nodesById.get(cursor));
    cursor = parentOf(cursor, idx);
  }
  return chain.reverse();
}

function setList(listEl, items, onClick) {
  clear(listEl);
  if (!items.length) {
    const li = document.createElement("li");
    li.textContent = "(none)";
    listEl.appendChild(li);
    return;
  }
  for (const item of items) {
    const li = document.createElement("li");
    const btn = document.createElement("button");
    btn.className = "linkish";
    btn.textContent = item.label;
    btn.type = "button";
    btn.addEventListener("click", () => onClick(item.id));
    li.appendChild(btn);
    listEl.appendChild(li);
  }
}

function ensureDefs() {
  const defs = document.createElementNS(NS, "defs");
  const markers = [
    { id: "arrow-contains", color: getCssVar("--edge-contains") },
    { id: "arrow-cites", color: getCssVar("--edge-cites") },
  ];

  for (const markerDef of markers) {
    const marker = document.createElementNS(NS, "marker");
    marker.setAttribute("id", markerDef.id);
    marker.setAttribute("markerWidth", "9");
    marker.setAttribute("markerHeight", "9");
    marker.setAttribute("refX", "8");
    marker.setAttribute("refY", "4.5");
    marker.setAttribute("orient", "auto");
    marker.setAttribute("markerUnits", "userSpaceOnUse");

    const path = document.createElementNS(NS, "path");
    path.setAttribute("d", "M 0 0 L 9 4.5 L 0 9 z");
    path.setAttribute("fill", markerDef.color);
    marker.appendChild(path);
    defs.appendChild(marker);
  }

  svg.appendChild(defs);
}

function drawCurvedEdge(path, a, b, edgeType = "contains", curvatureSeed = 0.5) {
  const dx = b.x - a.x;
  const dy = b.y - a.y;
  const distance = Math.hypot(dx, dy) || 1;
  const normalX = -dy / distance;
  const normalY = dx / distance;
  const direction = curvatureSeed >= 0.5 ? 1 : -1;
  const bendBase = edgeType === "cites" ? 0.2 : 0.12;
  const bend = Math.min(140, distance * bendBase) * direction;

  const c1x = a.x + dx * 0.33 + normalX * bend;
  const c1y = a.y + dy * 0.33 + normalY * bend;
  const c2x = a.x + dx * 0.66 + normalX * bend;
  const c2y = a.y + dy * 0.66 + normalY * bend;

  path.setAttribute("d", `M ${a.x} ${a.y} C ${c1x} ${c1y}, ${c2x} ${c2y}, ${b.x} ${b.y}`);
  path.setAttribute("class", `edge ${edgeType}`);
  path.setAttribute("marker-end", `url(#arrow-${edgeType})`);
}

function updateNodeVisual(node, visual, pos, options = {}) {
  const radius = visual.radius;
  const anchorLeft = pos.x < options.centerX;
  const labelOffset = radius + 11;
  const labelMax = options.shapeMode === "shape-key" ? 32 : node.node_type === "source" ? 26 : 42;
  const label = options.focused || options.hovered ? node.label : shortLabel(node.label, labelMax);

  if (visual.shape.tagName === "circle") {
    visual.shape.setAttribute("cx", pos.x);
    visual.shape.setAttribute("cy", pos.y);
  } else if (visual.shape.tagName === "rect") {
    if (node.node_type === "root") {
      visual.shape.setAttribute("x", pos.x - radius);
      visual.shape.setAttribute("y", pos.y - radius);
      visual.shape.setAttribute("width", radius * 2);
      visual.shape.setAttribute("height", radius * 2);
    } else {
      visual.shape.setAttribute("x", pos.x - radius);
      visual.shape.setAttribute("y", pos.y - radius * 0.8);
      visual.shape.setAttribute("width", radius * 2);
      visual.shape.setAttribute("height", radius * 1.6);
    }
  } else {
    visual.shape.setAttribute(
      "points",
      `${pos.x},${pos.y - radius} ${pos.x + radius},${pos.y} ${pos.x},${pos.y + radius} ${pos.x - radius},${pos.y}`,
    );
  }

  visual.group.setAttribute("transform", `translate(0 0)`);
  visual.group.classList.toggle("focus", Boolean(options.focused));
  visual.group.classList.toggle("hovered", Boolean(options.hovered));

  visual.text.setAttribute("x", anchorLeft ? pos.x - labelOffset : pos.x + labelOffset);
  visual.text.setAttribute("y", pos.y + 4);
  visual.text.setAttribute("text-anchor", anchorLeft ? "end" : "start");
  visual.text.textContent = label;

  if (visual.typeText) {
    visual.typeText.setAttribute("x", anchorLeft ? pos.x - labelOffset : pos.x + labelOffset);
    visual.typeText.setAttribute("y", pos.y + 19);
    visual.typeText.setAttribute("text-anchor", anchorLeft ? "end" : "start");
  }
}

function svgPointFromEvent(event) {
  const point = svg.createSVGPoint();
  point.x = event.clientX;
  point.y = event.clientY;
  return point.matrixTransform(svg.getScreenCTM().inverse());
}

function createNodeVisual(node, pos, radius, options) {
  const group = document.createElementNS(NS, "g");
  group.setAttribute("class", `node ${node.node_type}`);
  group.style.cursor = options.draggable ? "grab" : "pointer";

  let shape;
  if (options.shapeMode === "shape-key") {
    if (node.node_type === "root") {
      shape = document.createElementNS(NS, "rect");
      shape.setAttribute("rx", "6");
    } else if (node.node_type === "section") {
      shape = document.createElementNS(NS, "rect");
      shape.setAttribute("rx", "12");
    } else if (node.node_type === "source") {
      shape = document.createElementNS(NS, "polygon");
    } else {
      shape = document.createElementNS(NS, "circle");
    }
  } else {
    shape = document.createElementNS(NS, node.node_type === "source" ? "polygon" : "circle");
  }
  shape.setAttribute("fill", colors[node.node_type] || "#888");

  const text = document.createElementNS(NS, "text");
  text.setAttribute("class", "node-label");

  let typeText = null;
  if (options.showType) {
    typeText = document.createElementNS(NS, "text");
    typeText.setAttribute("class", "node-type");
    typeText.textContent = node.node_type;
  }

  const visual = { group, shape, text, typeText, radius };
  updateNodeVisual(node, visual, pos, options);

  group.appendChild(shape);
  group.appendChild(text);
  if (typeText) group.appendChild(typeText);

  let dragState = null;

  if (options.draggable) {
    group.addEventListener("pointerdown", (event) => {
      event.preventDefault();
      const start = svgPointFromEvent(event);
      dragState = { pointerId: event.pointerId, moved: false, start };
      group.setPointerCapture(event.pointerId);
      group.style.cursor = "grabbing";
      options.onDragStart?.(node.id);
    });

    group.addEventListener("pointermove", (event) => {
      if (!dragState || dragState.pointerId !== event.pointerId) return;
      const point = svgPointFromEvent(event);
      const dx = point.x - dragState.start.x;
      const dy = point.y - dragState.start.y;
      if (!dragState.moved && Math.hypot(dx, dy) > 4) dragState.moved = true;
      options.onDragMove?.(node.id, point);
    });

    const endDrag = (event) => {
      if (!dragState || dragState.pointerId !== event.pointerId) return;
      group.releasePointerCapture(event.pointerId);
      group.style.cursor = "grab";
      options.onDragEnd?.(node.id);
      group.dataset.dragMoved = dragState.moved ? "1" : "";
      dragState = null;
    };

    group.addEventListener("pointerup", endDrag);
    group.addEventListener("pointercancel", endDrag);
  }

  group.addEventListener("mouseenter", () => options.onHover?.(node.id));
  group.addEventListener("mouseleave", () => options.onHover?.(null));
  group.addEventListener("click", () => {
    if (group.dataset.dragMoved === "1") {
      group.dataset.dragMoved = "";
      return;
    }
    options.onSelect(node.id);
  });

  return visual;
}

function drawHierarchyMap(focusId, idx, onSelect) {
  clear(svg);
  setViewBox(HIERARCHY_VIEW);
  ensureDefs();

  const focusNode = idx.nodesById.get(focusId);
  if (!focusNode) return;

  const cx = HIERARCHY_VIEW.width / 2;
  const cy = HIERARCHY_VIEW.height / 2;

  const parentId = parentOf(focusId, idx);
  const childNodes = childrenOf(focusId, idx);
  const sourceNodes = sourcesOf(focusId, idx);

  const positions = new Map();
  positions.set(focusId, { x: cx, y: cy });
  if (parentId) positions.set(parentId, { x: cx, y: cy - 215 });

  childNodes.forEach((child, i) => {
    positions.set(child.id, polar(cx, cy, 225, i, Math.max(childNodes.length, 1)));
  });
  sourceNodes.forEach((source, i) => {
    positions.set(source.id, polar(cx, cy, 330, i, Math.max(sourceNodes.length, 1)));
  });

  const renderIds = [focusId];
  if (parentId) renderIds.push(parentId);
  renderIds.push(...childNodes.map((n) => n.id));
  renderIds.push(...sourceNodes.map((n) => n.id));

  const edgeGroup = document.createElementNS(NS, "g");
  edgeGroup.setAttribute("class", "edges-layer");
  svg.appendChild(edgeGroup);
  if (parentId) {
    const path = document.createElementNS(NS, "path");
    drawCurvedEdge(path, positions.get(parentId), positions.get(focusId), "contains", hash01(`${parentId}:${focusId}`));
    edgeGroup.appendChild(path);
  }
  for (const child of childNodes) {
    const path = document.createElementNS(NS, "path");
    drawCurvedEdge(path, positions.get(focusId), positions.get(child.id), "contains", hash01(`${focusId}:${child.id}`));
    edgeGroup.appendChild(path);
  }
  for (const source of sourceNodes) {
    const path = document.createElementNS(NS, "path");
    drawCurvedEdge(path, positions.get(focusId), positions.get(source.id), "cites", hash01(`${focusId}:${source.id}`));
    edgeGroup.appendChild(path);
  }

  const nodeGroup = document.createElementNS(NS, "g");
  nodeGroup.setAttribute("class", "nodes-layer");
  svg.appendChild(nodeGroup);
  for (const id of renderIds) {
    const node = idx.nodesById.get(id);
    const pos = positions.get(id);
    const radius = node.node_type === "root" ? 28 : node.node_type === "source" ? 13 : 18;
    const visual = createNodeVisual(node, pos, radius, {
      focused: id === focusId,
      hovered: false,
      centerX: cx,
      onSelect,
      shapeMode: "shape-key",
      showType: id !== focusId,
      draggable: false,
    });
    nodeGroup.appendChild(visual.group);
  }
}

function visibleTypes() {
  return new Set(
    Array.from(flatFilters.querySelectorAll('input[type="checkbox"]:checked')).map((input) => input.dataset.type),
  );
}

function seedFlatNode(node, view) {
  const centerX = view.width / 2;
  const centerY = view.height / 2;
  const minDimension = Math.min(view.width, view.height);
  const ringRadius = minDimension * TYPE_RING[node.node_type];
  const angle = hash01(`${node.id}:angle`) * Math.PI * 2;
  const drift = (hash01(`${node.id}:drift`) - 0.5) * minDimension * 0.08;

  return {
    x: centerX + Math.cos(angle) * (ringRadius + drift),
    y: centerY + Math.sin(angle) * (ringRadius + drift),
  };
}

function ensureFlatNodeState(node) {
  if (!flatState.positions.has(node.id)) flatState.positions.set(node.id, seedFlatNode(node, FLAT_VIEW));
  if (!flatState.velocities.has(node.id)) flatState.velocities.set(node.id, { x: 0, y: 0 });
  if (!flatState.radii.has(node.id)) {
    const radius = node.node_type === "root" ? 18 : node.node_type === "source" ? 9 : 12;
    flatState.radii.set(node.id, radius);
  }
}

function updateFlatScene() {
  if (!flatState.visibleIds.length) return;

  for (const edgeVisual of flatState.edgeVisuals) {
    const sourcePos = flatState.positions.get(edgeVisual.source);
    const targetPos = flatState.positions.get(edgeVisual.target);
    if (sourcePos && targetPos) {
      drawCurvedEdge(edgeVisual.path, sourcePos, targetPos, edgeVisual.type, edgeVisual.curvatureSeed);
    }
  }

  const centerX = FLAT_VIEW.width / 2;
  for (const id of flatState.visibleIds) {
    const node = flatState.nodesById.get(id);
    const visual = flatState.nodeVisuals.get(id);
    const pos = flatState.positions.get(id);
    updateNodeVisual(node, visual, pos, {
      focused: id === flatState.focusId,
      hovered: id === flatState.hoveredId,
      centerX,
      shapeMode: "shape-key",
      showType: false,
    });
  }
}

function tickFlatLayout() {
  const ids = flatState.visibleIds;
  if (!ids.length) return;

  const centerX = FLAT_VIEW.width / 2;
  const centerY = FLAT_VIEW.height / 2;
  const minDimension = Math.min(FLAT_VIEW.width, FLAT_VIEW.height);
  const alpha = flatState.alpha;

  for (const id of ids) {
    const velocity = flatState.velocities.get(id);
    if (id === flatState.draggedId) {
      velocity.x = 0;
      velocity.y = 0;
      continue;
    }
    velocity.x *= 0.88;
    velocity.y *= 0.88;
  }

  for (let i = 0; i < ids.length; i += 1) {
    const idA = ids[i];
    const nodeA = flatState.nodesById.get(idA);
    const posA = flatState.positions.get(idA);
    const velA = flatState.velocities.get(idA);
    const frozenA = idA === flatState.draggedId;

    for (let j = i + 1; j < ids.length; j += 1) {
      const idB = ids[j];
      const posB = flatState.positions.get(idB);
      const velB = flatState.velocities.get(idB);
      const frozenB = idB === flatState.draggedId;
      let dx = posB.x - posA.x;
      let dy = posB.y - posA.y;
      let distSq = dx * dx + dy * dy;
      if (distSq < 36) {
        dx = (Math.random() - 0.5) * 2;
        dy = (Math.random() - 0.5) * 2;
        distSq = dx * dx + dy * dy;
      }
      const force = (minDimension * 0.32 * alpha) / distSq;
      if (!frozenA) {
        velA.x -= dx * force;
        velA.y -= dy * force;
      }
      if (!frozenB) {
        velB.x += dx * force;
        velB.y += dy * force;
      }
    }

    const ring = minDimension * TYPE_RING[nodeA.node_type];
    const angle = hash01(`${idA}:angle`) * Math.PI * 2;
    const targetX = centerX + Math.cos(angle) * ring;
    const targetY = centerY + Math.sin(angle) * ring;
    if (!frozenA) {
      velA.x += (targetX - posA.x) * 0.0014 * alpha;
      velA.y += (targetY - posA.y) * 0.0014 * alpha;
      velA.x += (centerX - posA.x) * 0.00015 * alpha;
      velA.y += (centerY - posA.y) * 0.00015 * alpha;
    }
  }

  for (const edge of flatState.renderEdges || []) {
    const posA = flatState.positions.get(edge.source);
    const posB = flatState.positions.get(edge.target);
    const velA = flatState.velocities.get(edge.source);
    const velB = flatState.velocities.get(edge.target);
    const frozenA = edge.source === flatState.draggedId;
    const frozenB = edge.target === flatState.draggedId;
    const dx = posB.x - posA.x;
    const dy = posB.y - posA.y;
    const distance = Math.hypot(dx, dy) || 1;
    const desired = edge.type === "contains" ? 120 : 86;
    const spring = edge.type === "contains" ? 0.0032 : 0.002;
    const force = (distance - desired) * spring * alpha;
    const fx = (dx / distance) * force;
    const fy = (dy / distance) * force;
    if (!frozenA) {
      velA.x += fx;
      velA.y += fy;
    }
    if (!frozenB) {
      velB.x -= fx;
      velB.y -= fy;
    }
  }

  for (const id of ids) {
    if (id === flatState.draggedId) continue;
    const pos = flatState.positions.get(id);
    const vel = flatState.velocities.get(id);
    pos.x = clamp(pos.x + vel.x, 70, FLAT_VIEW.width - 70);
    pos.y = clamp(pos.y + vel.y, 70, FLAT_VIEW.height - 70);
  }

  flatState.alpha *= 0.985;
  updateFlatScene();

  if (flatState.alpha > 0.025) {
    flatState.animationFrame = requestAnimationFrame(tickFlatLayout);
  } else {
    flatState.animationFrame = 0;
    flatState.alpha = 0;
  }
}

function startFlatSimulation(alpha = 1) {
  flatState.alpha = Math.max(flatState.alpha, alpha);
  if (!flatState.animationFrame) {
    flatState.animationFrame = requestAnimationFrame(tickFlatLayout);
  }
}

function drawFlatOntologyMap(focusId, idx, onSelect) {
  cancelAnimationFrame(flatState.animationFrame);
  flatState.animationFrame = 0;
  flatState.draggedId = null;

  clear(svg);
  setViewBox(FLAT_VIEW);
  ensureDefs();

  const allowed = visibleTypes();
  const nodes = idx.nodes.filter((node) => allowed.has(node.node_type));
  const nodeIds = nodes.map((node) => node.id);
  const visibleIdSet = new Set(nodeIds);
  const renderEdges = idx.edges.filter((edge) => visibleIdSet.has(edge.source) && visibleIdSet.has(edge.target));

  flatState.nodeVisuals = new Map();
  flatState.edgeVisuals = [];
  flatState.nodesById = new Map(nodes.map((node) => [node.id, node]));
  flatState.visibleIds = nodeIds;
  flatState.renderEdges = renderEdges;
  flatState.focusId = focusId;

  for (const node of nodes) ensureFlatNodeState(node);

  const edgeGroup = document.createElementNS(NS, "g");
  edgeGroup.setAttribute("class", "edges-layer");
  svg.appendChild(edgeGroup);

  for (const edge of renderEdges) {
    const path = document.createElementNS(NS, "path");
    const curvatureSeed = hash01(`${edge.source}:${edge.target}:${edge.type}`);
    flatState.edgeVisuals.push({ path, source: edge.source, target: edge.target, type: edge.type, curvatureSeed });
    edgeGroup.appendChild(path);
  }

  const nodeGroup = document.createElementNS(NS, "g");
  nodeGroup.setAttribute("class", "nodes-layer");
  svg.appendChild(nodeGroup);

  for (const node of nodes) {
    const visual = createNodeVisual(node, flatState.positions.get(node.id), flatState.radii.get(node.id), {
      focused: node.id === focusId,
      hovered: node.id === flatState.hoveredId,
      centerX: FLAT_VIEW.width / 2,
      onSelect,
      shapeMode: "shape-key",
      showType: false,
      draggable: true,
      onHover: (id) => {
        flatState.hoveredId = id;
        updateFlatScene();
      },
      onDragStart: (id) => {
        flatState.draggedId = id;
        flatState.focusId = id;
        const velocity = flatState.velocities.get(id);
        velocity.x = 0;
        velocity.y = 0;
        updateFlatScene();
      },
      onDragMove: (id, point) => {
        const pos = flatState.positions.get(id);
        pos.x = clamp(point.x, 70, FLAT_VIEW.width - 70);
        pos.y = clamp(point.y, 70, FLAT_VIEW.height - 70);
        const velocity = flatState.velocities.get(id);
        velocity.x = 0;
        velocity.y = 0;
        updateFlatScene();
      },
      onDragEnd: (id) => {
        if (flatState.draggedId === id) flatState.draggedId = null;
        startFlatSimulation(0.18);
      },
    });
    flatState.nodeVisuals.set(node.id, visual);
    nodeGroup.appendChild(visual.group);
  }

  updateFlatScene();
  startFlatSimulation(1);
}

function updatePanel(focusId, idx, onSelect) {
  const node = idx.nodesById.get(focusId);
  focusTitle.textContent = node.label;
  focusMeta.textContent = `${node.node_type} • level ${node.level}${node.meta?.path ? ` • ${node.meta.path}` : ""}`;

  setList(childrenList, childrenOf(focusId, idx), onSelect);
  setList(sourcesList, sourcesOf(focusId, idx), onSelect);

  clear(breadcrumb);
  for (const ancestor of lineage(focusId, idx)) {
    const li = document.createElement("li");
    const btn = document.createElement("button");
    btn.className = "linkish";
    btn.type = "button";
    btn.textContent = ancestor.label;
    btn.addEventListener("click", () => onSelect(ancestor.id));
    li.appendChild(btn);
    breadcrumb.appendChild(li);
  }
}

function init(graph) {
  const idx = graphIndex(graph);
  let focusId = "thesis";
  let viewMode = "hierarchy";

  function select(id) {
    focusId = id;
    flatState.focusId = id;
    render();
  }

  function setMode(mode) {
    viewMode = mode;
    hierarchyBtn.classList.toggle("active", mode === "hierarchy");
    flatBtn.classList.toggle("active", mode === "flat");
    flatFilters.classList.toggle("hidden", mode !== "flat");
    render();
  }

  function render() {
    if (viewMode === "flat") {
      drawFlatOntologyMap(focusId, idx, select);
    } else {
      cancelAnimationFrame(flatState.animationFrame);
      flatState.animationFrame = 0;
      drawHierarchyMap(focusId, idx, select);
    }
    updatePanel(focusId, idx, select);
  }

  hierarchyBtn.addEventListener("click", () => setMode("hierarchy"));
  flatBtn.addEventListener("click", () => setMode("flat"));

  for (const input of flatFilters.querySelectorAll('input[type="checkbox"]')) {
    input.addEventListener("change", render);
  }

  homeBtn.addEventListener("click", () => select("thesis"));
  upBtn.addEventListener("click", () => {
    const parent = parentOf(focusId, idx);
    if (parent) select(parent);
  });

  setMode("hierarchy");
}

loadGraph().then(init).catch((err) => {
  focusTitle.textContent = "Error loading graph";
  focusMeta.textContent = err.message;
});
