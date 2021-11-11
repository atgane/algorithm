# 백준 17435

import sys
ssr = sys.stdin.readline

N = int(ssr())
arr = [0] + list(map(int, ssr().split()))
table = [[arr[i] for i in range(N + 1)]]

Q = int(ssr())
for _ in range(Q):
    t1, t2 = list(map(int, ssr().split()))
    start = t2
    i = 0
    while t1 >= 1 << i:
        if len(table) - 1 < i:
            table.append([])
            for j in range(N + 1):
                table[i].append(table[i - 1][table[i - 1][j]])
        if t1 & 1 << i > 0:
            start = table[i][start]
        i += 1
    print(start)