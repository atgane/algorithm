# _graph(list): 간선의 정보를 담은 리스트
# _graph[][0](int): 시작 정점
# _graph[][1](int): 도착 정점
# _graph[][2](float): 가중치
# _V(int): 정점의 개수
# _E(int): 간선의 개수
# _start(int): 시작 정점의 번호
# return: _start 정점에서 다른 모든 정점의 최단거리

def Bellan_Ford(_graph, _V, _E, _start, INF=1e15):
    _ans = [INF for _ in range(_V + 1)]
    _ans[_start] = 0
    for i in range(_V - 1):
        for j in range(_E):
            cur, next_node, cost = _graph[j]
            if _ans[cur] != INF and _ans[cur] + cost < _ans[next_node]:
                _ans[next_node] = _ans[cur] + cost
    return _ans

def Bellan_Ford_one_loop(_graph, _E,  _weight, INF=1e15):
    for j in range(_E):
        cur, next_node, cost = _graph[j]
        if _weight[cur] != INF and _weight[cur] + cost < _weight[next_node]:
            _weight[next_node] = _weight[cur] + cost
            """return True # 계속 값이 작아지기 때문
    return False """