const svg = document.getElementById("map");
const NS = "http://www.w3.org/2000/svg";

const focusTitle = document.getElementById("focus-title");
const focusMeta = document.getElementById("focus-meta");
const childrenList = document.getElementById("children-list");
const sourcesList = document.getElementById("sources-list");
const breadcrumb = document.getElementById("breadcrumb");

const homeBtn = document.getElementById("home-btn");
const upBtn = document.getElementById("up-btn");

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

function shortLabel(label, max = 30) {
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

  return { nodesById, outgoing, incoming };
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

function drawMap(focusId, idx, onSelect) {
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

  function drawEdge(aId, bId) {
    const a = positions.get(aId);
    const b = positions.get(bId);
    if (!a || !b) return;
    const path = document.createElementNS(NS, "path");
    const mx = (a.x + b.x) / 2;
    const my = (a.y + b.y) / 2;
    const c1x = (a.x + mx) / 2;
    const c1y = (a.y + my) / 2 - 16;
    const c2x = (b.x + mx) / 2;
    const c2y = (b.y + my) / 2 + 16;
    path.setAttribute("d", `M ${a.x} ${a.y} C ${c1x} ${c1y}, ${c2x} ${c2y}, ${b.x} ${b.y}`);
    path.setAttribute("class", "edge");
    edgeGroup.appendChild(path);
  }

  if (parentId) drawEdge(parentId, focusId);
  for (const child of childNodes) drawEdge(focusId, child.id);
  for (const source of sourceNodes) drawEdge(focusId, source.id);

  const nodeGroup = document.createElementNS(NS, "g");
  svg.appendChild(nodeGroup);

  for (const id of renderIds) {
    const node = idx.nodesById.get(id);
    const { x, y } = positions.get(id);
    const group = document.createElementNS(NS, "g");
    group.setAttribute("class", `node${id === focusId ? " focus" : ""}`);
    group.style.cursor = "pointer";

    const circle = document.createElementNS(NS, "circle");
    const radius = node.node_type === "root" ? 50 : node.node_type === "source" ? 24 : 34;
    circle.setAttribute("cx", x);
    circle.setAttribute("cy", y);
    circle.setAttribute("r", radius);
    circle.setAttribute("fill", colors[node.node_type] || "#888");

    const text = document.createElementNS(NS, "text");
    text.setAttribute("x", x);
    text.setAttribute("y", y + 4);
    text.textContent = shortLabel(node.label, node.node_type === "source" ? 18 : 24);

    const label2 = document.createElementNS(NS, "text");
    label2.setAttribute("x", x);
    label2.setAttribute("y", y + radius + 16);
    label2.setAttribute("fill", "#9ca4be");
    label2.textContent = node.node_type;

    group.appendChild(circle);
    group.appendChild(text);
    if (id !== focusId) group.appendChild(label2);

    group.addEventListener("click", () => onSelect(id));
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

  function select(id) {
    focusId = id;
    drawMap(focusId, idx, select);
    updatePanel(focusId, idx, select);
  }

  homeBtn.addEventListener("click", () => select("thesis"));
  upBtn.addEventListener("click", () => {
    const parent = parentOf(focusId, idx);
    if (parent) select(parent);
  });

  select(focusId);
}

loadGraph().then(init).catch((err) => {
  focusTitle.textContent = "Error loading graph";
  focusMeta.textContent = err.message;
});
