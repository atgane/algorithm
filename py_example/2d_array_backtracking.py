from collections import deque
import sys
import copy
ssr = sys.stdin.readline

M, N = list(map(int, ssr().split()))
arr = [list(map(int, ssr().split())) for _ in range(M)]

def check_init_location(_M, _N, _arr):
    _ans1 = []
    _ans2 = []
    for y in range(_M):
        for x in range(_N):
            if _arr[y][x] == 0 and len(_ans2) < 3:
                _ans2.append([y, x])
            if _arr[y][x] == 2:
                _ans1.append([y, x])
    return _ans1, _ans2

def count_zero(_M, _N, _arr):
    _ans = 0
    for y in range(_M):
        for x in range(_N):
            if _arr[y][x] == 0:
                _ans += 1
    return _ans

def dfs(_init_location, _M, _N, _arr):
    _stack = copy.deepcopy(_init_location)  
    while _stack:
        tmp_loc = _stack.pop()
        _dy = [0, 0, -1, 1]
        _dx = [1, -1, 0, 0]
        for i in range(4):
            _y = _dy[i] + tmp_loc[0]
            _x = _dx[i] + tmp_loc[1]
            if 0 <= _x < _N and 0 <= _y < _M:
                if _arr[_y][_x] == 0:
                    _arr[_y][_x] = 2
                    _stack.append([_y, _x])

def backtrack(_back_init_location, _M, _N, _arr):
    _back_stack = copy.deepcopy(_back_init_location)
    _ans = 0
    while _back_stack:
        if len(_back_stack) == 3:
            _new_arr = copy.deepcopy(_arr)
            for _location in _back_stack:
                _new_arr[_location[0]][_location[1]] = 1
            _stack, _ = check_init_location(M, N, _new_arr)
            dfs(_stack, _M, _N, _new_arr)
            _zero = count_zero(_M, _N, _new_arr)
            if _zero > _ans:
                _ans = _zero
        _tmp_loc = _back_stack.pop()
        while len(_back_stack) < 3:
            _flag = 0
            for y in range(_tmp_loc[0], _M):
                for x in range(_tmp_loc[1] + 1 if y == _tmp_loc[0] else 0, _N):
                    if _arr[y][x] == 0:
                        _tmp_loc = [y, x]
                        _back_stack.append(_tmp_loc)
                        _flag = 1
                        break
                if _flag == 1:
                    break
            if _flag == 0:
                break
    return _ans

stack, back_stack = check_init_location(M, N, arr)
print(backtrack(back_stack, M, N, arr))