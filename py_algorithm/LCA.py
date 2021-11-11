import math

# table = []
# parent(list): 크기가 N + 1인 리스트. 각 노드의 부모를 저장
# N(int): 노드의 수

def calc_table(table, parent, N):
    table.append(parent)
    table_length = int(math.log2(N + 1)) + 1
    for i in range(1, table_length):
        table.append([])
        for j in range(N + 1):
            table[i].append(table[i - 1][table[i - 1][j]])

# depth[list]: 크기가 N + 1인 리스트, 각 노드의 깊이를 저장
# table: calc_table의 결과
# node1(int), node2(int): lca를 찾을 노드

def lca(node1, node2, depth, table):
    if depth[node1] < depth[node2]:
        node1, node2 = node2, node1
    
    log = len(table) - 1
    for i in range(log, -1, -1):
        if depth[node1] - depth[node2] >= (1 << i): node1 = table[i][node1]
    if node1 == node2: return node1
    for i in range(log, -1, -1):
        if table[i][node1] != table[i][node2]: node1, node2 = table[i][node1], table[i][node2]
    return table[0][node1]