# _V(int): 정점의 개수
# _E(int): 간선의 개수
# _graph(list): 간선의 정보를 담는 원소가 3인 리스트를 원소로 갖는 리스트
# _graph[][0](int): 시작 정점 번호
# _graph[][1](int): 도착 정점 번호
# _graph[][2](float): 간선의 가중치
# return: 최소신장트리 비용

def kruskal_algorithm(_V, _E, _graph):
    _graph = sorted(_graph, key=lambda x: x[2])
    parent_list = list(range(_V + 1))
    
    def find_parent(_node, _arr):
        if _arr[_node] != _node:
            _arr[_node] = find_parent(_arr[_node], _arr)
            return _arr[_node]
        return _node
        
    def union(_node1, _node2, _parent_list):
        _root1 = find_parent(_node1, _parent_list)
        _root2 = find_parent(_node2, _parent_list)
        _parent_list[_root1] = _root2

    tree_weight = 0

    for node1, node2, weight in _graph:
        if find_parent(node1, parent_list) != find_parent(node2, parent_list):
            union(node1, node2, parent_list)
            tree_weight += weight

    return tree_weight