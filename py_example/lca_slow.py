import sys
from collections import deque
ssr = sys.stdin.readline

def calc_depth(root, child, depth):
    depth[root] = 0
    queue = deque([root])
    while queue:
        t = queue.popleft()
        for i in child[t]:
            queue.append(i)
            depth[i] = depth[t] + 1

def lca(node1, node2, parent, depth):
    if depth[node1] < depth[node2]:
            node1, node2 = node2, node1

    while depth[node1] != depth[node2]:
        node1 = parent[node1]
    
    while True:
        if node1 == node2:
            return node1
        else:
            node1 = parent[node1]
            node2 = parent[node2]

T = int(ssr())
for _ in range(T):
    N = int(ssr())
    parent = [0 for _ in range(N + 1)]
    child = [[] for _ in range(N + 1)]
    depth = [0 for _ in range(N + 1)]
    for _ in range(N - 1):
        t1, t2 = list(map(int, ssr().split()))
        parent[t2] = t1
        child[t1].append(t2)
    t1, t2 = list(map(int, ssr().split()))
    root = parent[1:].index(0) + 1
    calc_depth(root, child, depth)
    print(lca(t1, t2, parent, depth))