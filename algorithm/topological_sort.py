# _graph(list): 간선의 정보를 담은 리스트
# _graph[][0](int): 출발 정점의 번호
# _graph[][1](int): 도착 정점의 번호
# _V(int): 정점 개수
# _E(int): 간선 개수
# return: 위상정렬된 리스트

def topological_sort(_graph, _V, _E):
    _node_list = [[] for _ in range(_V + 1)]
    _cnt_list = [0 for _ in range(_V + 1)]
    _stack = []
    _ans = []
    for _a, _b in _graph:
        _node_list[_a].append(_b)
        _cnt_list[_b] += 1
    
    for i in range(1, _V + 1):
        if _cnt_list[i] == 0:
            _stack.append(i)

    while _stack:
        _tmp = _stack.pop()
        _ans.append(_tmp)
        for _node in _node_list[_tmp]:
            _cnt_list[_node] -= 1
            if _cnt_list[_node] == 0:
                _stack.append(_node)
    
    return _ans