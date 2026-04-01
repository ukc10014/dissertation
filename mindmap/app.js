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

const colors = {
  root: getCssVar("--root"),
  document: getCssVar("--document"),
  section: getCssVar("--section"),
  source: getCssVar("--source"),
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

function drawEdge(edgeGroup, a, b, edgeType = "contains") {
  const path = document.createElementNS(NS, "path");
  const mx = (a.x + b.x) / 2;
  const my = (a.y + b.y) / 2;
  const c1x = (a.x + mx) / 2;
  const c1y = (a.y + my) / 2 - 16;
  const c2x = (b.x + mx) / 2;
  const c2y = (b.y + my) / 2 + 16;
  path.setAttribute("d", `M ${a.x} ${a.y} C ${c1x} ${c1y}, ${c2x} ${c2y}, ${b.x} ${b.y}`);
  path.setAttribute("class", `edge ${edgeType}`);
  edgeGroup.appendChild(path);
}

function renderNode(group, node, pos, radius, focused, onSelect, shapeMode = "circle") {
  const nodeClass = `node ${node.node_type}${focused ? " focus" : ""}`;
  group.setAttribute("class", nodeClass);
  group.style.cursor = "pointer";

  let shape;
  if (shapeMode === "shape-key") {
    if (node.node_type === "root") {
      shape = document.createElementNS(NS, "rect");
      shape.setAttribute("x", pos.x - radius);
      shape.setAttribute("y", pos.y - radius);
      shape.setAttribute("width", radius * 2);
      shape.setAttribute("height", radius * 2);
      shape.setAttribute("rx", "4");
    } else if (node.node_type === "section") {
      shape = document.createElementNS(NS, "rect");
      shape.setAttribute("x", pos.x - radius);
      shape.setAttribute("y", pos.y - radius * 0.8);
      shape.setAttribute("width", radius * 2);
      shape.setAttribute("height", radius * 1.6);
      shape.setAttribute("rx", "10");
    } else if (node.node_type === "source") {
      shape = document.createElementNS(NS, "polygon");
      shape.setAttribute(
        "points",
        `${pos.x},${pos.y - radius} ${pos.x + radius},${pos.y} ${pos.x},${pos.y + radius} ${pos.x - radius},${pos.y}`,
      );
    } else {
      shape = document.createElementNS(NS, "circle");
      shape.setAttribute("cx", pos.x);
      shape.setAttribute("cy", pos.y);
      shape.setAttribute("r", radius);
    }
  } else {
    shape = document.createElementNS(NS, "circle");
    shape.setAttribute("cx", pos.x);
    shape.setAttribute("cy", pos.y);
    shape.setAttribute("r", radius);
  }

  shape.setAttribute("fill", colors[node.node_type] || "#888");

  const text = document.createElementNS(NS, "text");
  text.setAttribute("x", pos.x + radius + 8);
  text.setAttribute("y", pos.y + radius + 12);
  text.setAttribute("class", "node-label");
  text.textContent = shortLabel(node.label, node.node_type === "source" ? 28 : 44);

  const type = document.createElementNS(NS, "text");
  type.setAttribute("x", pos.x + radius + 8);
  type.setAttribute("y", pos.y + radius + 27);
  type.setAttribute("class", "node-type");
  type.textContent = node.node_type;

  group.appendChild(shape);
  group.appendChild(text);
  if (!focused) group.appendChild(type);
  group.addEventListener("click", () => onSelect(node.id));
}

function drawHierarchyMap(focusId, idx, onSelect) {
  clear(svg);
  const focusNode = idx.nodesById.get(focusId);
  if (!focusNode) return;

  const viewBox = svg.viewBox.baseVal;
  const cx = viewBox.width / 2;
  const cy = viewBox.height / 2;

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
    positions.set(source.id, polar(cx, cy, 320, i, Math.max(sourceNodes.length, 1)));
  });

  const renderIds = [focusId];
  if (parentId) renderIds.push(parentId);
  renderIds.push(...childNodes.map((n) => n.id));
  renderIds.push(...sourceNodes.map((n) => n.id));

  const edgeGroup = document.createElementNS(NS, "g");
  svg.appendChild(edgeGroup);
  if (parentId) drawEdge(edgeGroup, positions.get(parentId), positions.get(focusId), "contains");
  for (const child of childNodes) drawEdge(edgeGroup, positions.get(focusId), positions.get(child.id), "contains");
  for (const source of sourceNodes) drawEdge(edgeGroup, positions.get(focusId), positions.get(source.id), "cites");

  const nodeGroup = document.createElementNS(NS, "g");
  svg.appendChild(nodeGroup);
  for (const id of renderIds) {
    const node = idx.nodesById.get(id);
    const pos = positions.get(id);
    const group = document.createElementNS(NS, "g");
    const radius = node.node_type === "root" ? 42 : node.node_type === "source" ? 18 : 28;
    renderNode(group, node, pos, radius, id === focusId, onSelect, "circle");
    nodeGroup.appendChild(group);
  }
}

function visibleTypes() {
  return new Set(
    Array.from(flatFilters.querySelectorAll('input[type="checkbox"]:checked')).map((input) => input.dataset.type),
  );
}

function drawFlatOntologyMap(focusId, idx, onSelect) {
  clear(svg);
  const allowed = visibleTypes();
  const nodes = idx.nodes.filter((n) => allowed.has(n.node_type));
  const view = svg.viewBox.baseVal;

  const order = ["root", "document", "section", "source"];
  const typeGroups = new Map(order.map((t) => [t, []]));
  for (const node of nodes) typeGroups.get(node.node_type)?.push(node);

  const columnX = new Map();
  order.forEach((type, i) => columnX.set(type, ((i + 1) * view.width) / (order.length + 1)));

  const positions = new Map();
  for (const type of order) {
    const group = typeGroups.get(type) || [];
    group.forEach((node, i) => {
      const step = view.height / (group.length + 1);
      positions.set(node.id, {
        x: columnX.get(type),
        y: (i + 1) * step,
      });
    });
  }

  const edgeGroup = document.createElementNS(NS, "g");
  svg.appendChild(edgeGroup);
  for (const edge of idx.edges) {
    if (!positions.has(edge.source) || !positions.has(edge.target)) continue;
    drawEdge(edgeGroup, positions.get(edge.source), positions.get(edge.target), edge.type);
  }

  const nodeGroup = document.createElementNS(NS, "g");
  svg.appendChild(nodeGroup);
  for (const node of nodes) {
    const group = document.createElementNS(NS, "g");
    const radius = node.node_type === "root" ? 18 : node.node_type === "source" ? 12 : 15;
    renderNode(group, node, positions.get(node.id), radius, node.id === focusId, onSelect, "shape-key");
    nodeGroup.appendChild(group);
  }
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
      drawHierarchyMap(focusId, idx, select);
    }
    updatePanel(focusId, idx, select);
  }

  function select(id) {
    focusId = id;
    render();
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