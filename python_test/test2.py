import sys
ssr = sys.stdin.readline

import heapq

def dijkstra(_graph, _V, _E, _start):
    ans = [1e15 for _ in range(_V + 1)]
    ans[_start] = 0
    heap = [[0, _start]]
    while heap:
        datum_weight, datum_node = heapq.heappop(heap)
        for tmp_node, tmp_weight in _graph[datum_node]:
            new_weight = tmp_weight + datum_weight
            if new_weight < ans[tmp_node]:
                ans[tmp_node] = new_weight
                heapq.heappush(heap, [new_weight, tmp_node])
    return ans

ssr = sys.stdin.readline

V, E = list(map(int, ssr().split()))
start = int(ssr())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    tmp = list(map(int, ssr().split()))
    graph[tmp[0]].append([tmp[1], tmp[2]])
    
print(dijkstra(graph, V, E, start))