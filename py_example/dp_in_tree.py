# 백준 2213

import sys
sys.setrecursionlimit(10**6)
ssr = sys.stdin.readline

N = int(ssr())
weight = [0] + list(map(int, ssr().split()))
graph = [[] for _ in range(N + 1)]
ans1 = [0 for _ in range(N + 1)]
ans2 = [0 for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
path1 = [[] for _ in range(N + 1)]
path2 = [[] for _ in range(N + 1)]
for i in range(N - 1):
    t1, t2 = list(map(int, ssr().split()))
    graph[t1].append(t2)
    graph[t2].append(t1)

def func(node):
    visited[node] = True
    ans1[node] = weight[node]
    path1[node].append(node)
    for i in graph[node]:
        if not visited[i]:
            func(i)
            ans1[node] += ans2[i]
            for j in path2[i]:
                path1[node].append(j)
            if ans1[i] >= ans2[i]:
                ans2[node] += ans1[i]
                for j in path1[i]:
                    path2[node].append(j)
            else:
                ans2[node] += ans2[i]
                for j in path2[i]:
                    path2[node].append(j)

func(1)
val = ans1[1] if ans1[1] >= ans2[1] else ans2[1]
path = path1[1] if ans1[1] >= ans2[1] else path2[1]
path.sort()
print(val)
print(*path)