# _graph(list): 간선의 정보를 담은 리스트
# _graph[][0](int): 시작 정점
# _graph[][1](int): 도착 정점
# _graph[][2](float): 가중치
# _N(int): 정점 개수
# _M(int): 간선 개수
# return: 최단거리 행렬

def floyd_Warshall_algorithm(_graph, _N, _M, _inf=1e15):
    _matrix = [[0 if i == j else _inf for i in range(_N + 1)] for j in range(_N + 1)]

    for _node_data in _graph:
        _matrix[_node_data[0]][_node_data[1]] = min(_node_data[2], _matrix[_node_data[0]][_node_data[1]])

    for k in range(1, _N + 1):
        for i in range(1, _N + 1):
            for j in range(1, _N + 1):
                _matrix[i][j] = min(_matrix[i][j], _matrix[i][k] + _matrix[k][j])

    return _matrix