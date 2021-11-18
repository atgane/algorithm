# 백준 17136

import sys
ssr = sys.stdin.readline

graph = [list(map(int, ssr().split())) for _ in range(10)]
ans = 26
table = [0, 5, 5, 5, 5, 5]

def check(n, y, x):
    global graph
    for i in range(n):
        for j in range(n):
            if graph[y + i][x + j] == 0:
                return False
    return True

def set_num(n, y, x, k):
    global graph
    for i in range(n):
        for j in range(n):
            graph[y + i][x + j] = k

def dfs(y, x, cnt):
    global ans
    global table
    global graph
    continue_flag = False
    for i in range(10):
        for j in range(10):
            if graph[i][j] == 1:
                x, y = j, i
                continue_flag = True
                break
        if continue_flag:
            break
    if not continue_flag:
        ans = min(ans, cnt)
        return
    
    if ans <= cnt: return

    for i in range(1, 6):
        try:
            if check(i, y, x) and table[i] != 0:
                table[i] -= 1
                set_num(i, y, x, 0)
                dfs(y, x, cnt + 1)
                table[i] += 1
                set_num(i, y, x, 1)
        except:
            _ = 1

dfs(0, 0, 0)
if ans == 26: print(-1)
else: print(ans)