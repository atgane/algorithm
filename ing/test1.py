# https://www.acmicpc.net/problem/21298

import sys
ssr = sys.stdin.readline

dim = list(map(int, ssr().split()))
mat = []
def change_val(p, val): mat[p[0]][p[1]][p[2]][p[3]][p[4]][p[5]][p[6]][p[7]][p[8]][p[9]][p[10]] = val
def ret_point(p): return mat[p[0]][p[1]][p[2]][p[3]][p[4]][p[5]][p[6]][p[7]][p[8]][p[9]][p[10]]
def init(mat, n):
    for i in range(dim[n]):
        if n == 10:
            mat.append(0)
        else:
            mat.append([])
            sub_mat = mat[-1]
            init(sub_mat, n + 1)
def calc_point_loc(i):
    ans = [0 for _ in range(11)]
    for j in range(10, -1, -1):
        ans[j] = i % dim[j]
        i //= dim[j]
    return ans
def swap(p1, p2):
    mat[p1[0]][p1[1]][p1[2]][p1[3]][p1[4]][p1[5]][p1[6]][p1[7]][p1[8]][p1[9]][p1[10]], mat[p2[0]][p2[1]][p2[2]][p2[3]][p2[4]][p2[5]][p2[6]][p2[7]][p2[8]][p2[9]][p2[10]] =\
        mat[p2[0]][p2[1]][p2[2]][p2[3]][p2[4]][p2[5]][p2[6]][p2[7]][p2[8]][p2[9]][p2[10]], mat[p1[0]][p1[1]][p1[2]][p1[3]][p1[4]][p1[5]][p1[6]][p1[7]][p1[8]][p1[9]][p1[10]]
def sym_axis(axis, p1, p2):
    for i in range(10):
        if i != axis:
            dim1 = p1[i]; dim2 = p2[i]
            if dim1 > dim2:
                dim1, dim2 = dim2, dim1
            for j in range((dim2 - dim1) // 2):
                
                


# 입력.
init(mat, 0)
for i in range(dim[0] * dim[1] * dim[2] * dim[3] * dim[4] * dim[5] * dim[6] * dim[7] * dim[8] * dim[9]):
    t_arr = list(map(int, ssr().split()))
    for j in range(dim[10]):
        k = i * dim[10] + j
        point_loc = calc_point_loc(k)
        change_val(point_loc, t_arr[j])

M = int(ssr())
for i in range(M):
    s = list(map(int, ssr().split()))
    if (s[0] - 1) // 11 == 0:
        t = (s[0] - 1) % 11
        