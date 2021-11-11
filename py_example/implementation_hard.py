# 백준 13460 

import sys
ssr = sys.stdin.readline

N, M = map(int, ssr().split())
graph = [list(ssr()[:-1]) for _ in range(N)]

def check(ry, rx, by, bx, direction):
    if direction == 'u':
        flag = 0
        r_distance = 0
        b_distance = 0
        while graph[ry][rx] != '#':
            ry -= 1
            r_distance += 1
            if graph[ry][rx] == 'O':
                flag = 1
                break
        ry += 1
        r_distance -= 1
        while graph[by][bx] != '#':
            by -= 1
            b_distance += 1
            if graph[by][bx] == 'O':
                flag = -1
                break
        by += 1
        b_distance -= 1
        if flag == 1 or flag == -1:
            return [flag]
        elif ry == by and rx == bx:
            if  r_distance > b_distance: ry += 1
            else: by += 1
        return [0, ry, rx, by, bx]
        
    if direction == 'd':
        flag = 0
        r_distance = 0
        b_distance = 0
        while graph[ry][rx] != '#':
            ry += 1
            r_distance += 1
            if graph[ry][rx] == 'O':
                flag = 1
                break
        ry -= 1
        r_distance -= 1
        while graph[by][bx] != '#':
            by += 1
            b_distance += 1
            if graph[by][bx] == 'O':
                flag = -1
                break
        by -= 1
        b_distance -= 1
        if flag == 1 or flag == -1:
            return [flag]
        elif ry == by and rx == bx:
            if r_distance > b_distance: ry -= 1
            else: by -= 1
        return [0, ry, rx, by, bx]
    
    if direction == 'l':
        flag = 0
        r_distance = 0
        b_distance = 0
        while graph[ry][rx] != '#':
            rx -= 1
            r_distance += 1
            if graph[ry][rx] == 'O':
                flag = 1
                break
        rx += 1
        r_distance -= 1
        while graph[by][bx] != '#':
            bx -= 1
            b_distance += 1
            if graph[by][bx] == 'O':
                flag = -1
                break
        bx += 1
        b_distance -= 1
        if flag == 1 or flag == -1:
            return [flag]
        elif ry == by and rx == bx:
            if r_distance > b_distance: rx += 1
            else: bx += 1
        return [0, ry, rx, by, bx]
        
    if direction == 'r':
        flag = 0
        r_distance = 0
        b_distance = 0
        while graph[ry][rx] != '#':
            rx += 1
            r_distance += 1
            if graph[ry][rx] == 'O':
                flag = 1
                break
        rx -= 1
        r_distance -= 1
        while graph[by][bx] != '#':
            bx += 1
            b_distance += 1
            if graph[by][bx] == 'O':
                flag = -1
                break
        bx -= 1
        b_distance -= 1
        if flag == 1 or flag == -1:
            return [flag]
        elif ry == by and rx == bx:
            if r_distance > b_distance: rx -= 1
            else: bx -= 1
        return [0, ry, rx, by, bx]

rx, ry = 0, 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'R':
            ry = i
            rx = j
            break

bx, by = 0, 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'B':
            by = i
            bx = j
            break

direction_list = ['l', 'r', 'u', 'd']
ans = 11

def func(ry, rx, by, bx, num):
    global ans
    if num > 10: 
        return
    
    for direction in direction_list:
        ret_list = check(ry, rx, by, bx, direction)
        if ret_list[0] == 1:
            if ans > num + 1:
                ans = num + 1
                continue
        elif ret_list[0] == -1:
            continue
        else:
            if ry == ret_list[1] and rx == ret_list[2] and by == ret_list[3] and bx == ret_list[4]:
                continue
            
            if num >= ans:
                break
            graph[ry][rx] = '.'
            graph[by][bx] = '.'
            graph[ret_list[1]][ret_list[2]] = 'R'
            graph[ret_list[3]][ret_list[4]] = 'B'
            func(ret_list[1], ret_list[2], ret_list[3], ret_list[4], num + 1)
            graph[ret_list[1]][ret_list[2]] = '.'
            graph[ret_list[3]][ret_list[4]] = '.'
            graph[ry][rx] = 'R'
            graph[by][bx] = 'B'
            
func(ry, rx, by, bx, 0)
if ans == 11: print(-1)
else: print(ans)