# 백준 2042

import sys
ssr = sys.stdin.readline

def init(arr, tree, node, start, end):
    if start == end: 
        tree[node] = arr[start]
    else:
        tree[node] = init(arr, tree, node * 2, start, (start + end) // 2) + init(arr, tree, node * 2 + 1, (start + end) // 2 + 1, end)
    return tree[node]

def func(tree, node, start, end, left, right):
    if left > end or right < start: return 0
    if left <= start and right >= end: return tree[node]
    return func(tree, node * 2, start, (start + end) // 2, left, right) + func(tree, node * 2 + 1, (start + end) // 2 + 1, end, left, right)

def update(tree, node, start, end, index, diff):
    if (index < start or index > end): return
    tree[node] = tree[node] + diff
    if start != end:
        update(tree, node * 2, start, (start + end) // 2, index, diff)
        update(tree, node * 2 + 1, (start + end) // 2 + 1, end, index, diff)

N, M, K = list(map(int, ssr().split()))
arr = [0] + [int(ssr()) for _ in range(N)]
x = 0
while len(arr) > 1 << x: x += 1
table = [0 for _ in range(1 + 1 << x)]
init(arr, table, 1, 1, len(arr) - 1)

for _ in range(M + K):
    t1, t2, t3 = list(map(int, ssr().split()))
    if t1 == 1:
        diff, arr[t2] = t3 - arr[t2], t3
        update(table, 1, 1, len(arr) - 1, t2, diff)
    else:
        print(func(table, 1, 1, len(arr) - 1, t2, t3))