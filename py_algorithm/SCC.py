# graph(list): 간선의 정보를 담은 리스트
# graph[][0](int): 출발 정점의 번호
# graph[][1](int): 도착 정점의 번호
# inv_graph(list): graph와 같으나 간선의 방향이 반대
# N(int): 노드의 개수

def find_scc(graph, inv_graph, N):
    def init_dfs(node, graph, visited, stack):
        visited[node] = True
        for child_node in graph[node]:
            if not visited[child_node]:
                init_dfs(child_node, graph, visited, stack)
        stack.append(node)

    visited = [False for _ in range(N + 1)]
    stack = []
    for i in range(1, N + 1):
        if not visited[i]:
            init_dfs(i, graph, visited, stack)

    def find_scc(node, inv_graph, local_scc, visited):
        visited[node] = True
        for child_node in inv_graph[node]:
            if not visited[child_node]:
                find_scc(child_node, inv_graph, local_scc, visited)
        local_scc.append(node)

    scc = []
    for i in range(N + 1): visited[i] = False
    for i in range(1, N + 1):
        node = stack.pop()
        if not visited[node]:
            local_scc = []
            find_scc(node, inv_graph, local_scc, visited)
            scc.append(local_scc)
    return scc