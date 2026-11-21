"""Q3: Dependency Graph Topological Sort & Cycle Detection."""
from collections import deque

def topological_sort(nodes, edges):
    indeg = {u: 0 for u in nodes}
    adj = {u: [] for u in nodes}
    for u, v in edges:
        adj[u].append(v)
        indeg[v] += 1

    q = deque([u for u in nodes if indeg[u] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    if len(order) != len(nodes):
        raise RuntimeError("Cyclic dependency detected in SDD!")
    return order

if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    edges = [(1, 2), (2, 3), (3, 9), (4, 5), (6, 7), (5, 8), (7, 8), (8, 9)]
    order = topological_sort(nodes, edges)
    print("Dependency Graph Topological Evaluation Order:", " -> ".join(map(str, order)))
