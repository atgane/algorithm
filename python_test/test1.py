import sys
ssr = sys.stdin.readline

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

V, E = list(map(int, ssr().split()))
graph = [list(map(int, ssr().split())) for _ in range(E)]

ans = topological_sort(graph, V, E)
for i in ans:
    print(i, end=' ')
    
print(V, E, graph)
print(ans)