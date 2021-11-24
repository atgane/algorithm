#백준 11505

import sys
ssr = sys.stdin.readline

def init(node, start, end):
    if start == end: 
        tree[node] = arr[start]
    else: 
        tree[node] = init(node * 2, start, (start + end) // 2) * init(node * 2 + 1, (start + end) // 2 + 1, end) % 1_000_000_007
    return tree[node]

def func(node, start, end, left, right):
    if left > end or right < start: return 1
    if left <= start and right >= end: return tree[node]
    return func(node * 2, start, (start + end) // 2, left, right) * func(node * 2 + 1, (start + end) // 2 + 1, end, left, right) % 1_000_000_007

def update(node, start, end, index, new_val):
    if index < start or end < index: return
    if index == start and index == end:
        tree[node] = new_val
    else:
        update(node * 2, start, (start + end) // 2, index, new_val)
        update(node * 2 + 1, (start + end) // 2 + 1, end, index, new_val)
        tree[node] = tree[node * 2] * tree[node * 2 + 1] % 1_000_000_007
    


N, M, K = map(int, ssr().split())
arr = [0] + [int(ssr()) for _ in range(N)]
x = 0
while len(arr) > 1 << x: x += 1
tree = [0 for _ in range(1 + 1 << x)]
init(1, 1, len(arr) - 1)
for _ in range(M + K):
    q1, q2, q3 = map(int, ssr().split())
    if q1 == 1:
        arr[q2] = q3
        update(1, 1, len(arr) - 1, q2, q3)
    else:
        print(func(1, 1, len(arr) - 1, q2, q3))