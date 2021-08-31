# _graph(list): 간선의 정보가 담긴 리스트를 원소로 갖는 리스트
# _graph[1](list): 1번 정점이 다른 정점과 연결된 정보를 담은 리스트(0번은 무시)
# ex) _data[1] = [[2, 3], [4, 5]]이면 1번 정점이 2번 정점과 3의 가중치로, 4번 정점과 5의 가중치로 유향연결됐다는 의미
# _V(int): 정점의 개수
# _E(int): 간선의 개수
# _start(int): 시작 정점의 번호
# return: _start 정점에서 다른 모든 정점의 최단거리

import heapq

def Dijkstra_Algorithm(_graph, _V, _E, _start):
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