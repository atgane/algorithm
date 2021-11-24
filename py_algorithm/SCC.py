# graph(list): 간선의 정보를 담은 리스트
# graph[i](list): graph의 i번째 노드가 어디로 도착할 수 있는지
# inv_graph(list): graph와 같으나 간선의 방향이 반대
# N(int): 노드의 개수
# scc(list): i번째 노드가 몇 번째 SCC에 포함되는지?
# scc_map(list): scc의 연결정보를 담은 리스트
# scc_map[i](list): scc의 i번째 노드가 어디로 도착할 수 있는지
# scc_num(int): scc의 개수

def find_scc(graph, inv_graph, N):
    def init_dfs(node):
        inner_stack = [node]
        while inner_stack:
            node = inner_stack[-1]
            visited[node] = True
            have_child_node = False
            for child_node in graph[node]:
                if not visited[child_node]:
                    inner_stack.append(child_node)
                    have_child_node = True
                    visited[child_node] = True
                    break
            if not have_child_node:
                stack.append(inner_stack.pop())


    visited = [False for _ in range(N + 1)]
    stack = []
    for i in range(1, N + 1):
        if not visited[i]:
            init_dfs(i)

    def find_scc(node, scc_num):
        inner_stack = [node]
        while inner_stack:
            node = inner_stack[-1]
            visited[node] = True
            have_child_node = False
            for child_node in inv_graph[node]:
                if not visited[child_node]:
                    inner_stack.append(child_node)
                    have_child_node = True
                    visited[child_node] = True
                    break
            if not have_child_node:
                scc[node] = scc_num
                inner_stack.pop()

    scc = [0 for _ in range(N + 1)]
    scc_num = 1

    for i in range(N + 1): visited[i] = False
    for i in range(1, N + 1):
        node = stack.pop()
        if not visited[node]:
            find_scc(node, scc_num)
            scc_num += 1
    scc_num -= 1
    scc_map = [[] for _ in range(scc_num + 1)]
    for node in range(1, N + 1):
        for child_node in graph[node]:
            if scc[node] != scc[child_node] and scc[child_node] not in scc_map[scc[node]]:
                scc_map[scc[node]].append(scc[child_node])
    return scc, scc_map, scc_num