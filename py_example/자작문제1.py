#백준 17615 유사문제: 다른 색도 옮길 수 있다면?

import sys
ssr = sys.stdin.readline

# 빨빨빨 + 파파파 + 파 -> 빨 파 arr1[i - 1] -> arr1[i]
# 파파파 + 빨빨빨 + 파 -> 빨 파 arr2[i - 1] + min(B[i - 1], R[i - 1]) -> arr1[i]
# 빨빨빨 + 파파파 + 파 -> 파 빨 arr1[i - 1] + min(B[i], R[i]) -> arr2[i]
# 파파파 + 빨빨빨 + 파 -> 파 빨 arr2[i - 1] + 1 -> arr2[i]
# ??????????????? + 파 -> 파 빨 R[i] -> arr2[i]

N = int(ssr())
ball_list = [0 if i == 'B' else 1 for i in ssr()[:-1]]
R = [1 if ball_list[0] == 1 else 0]
B = [0 if ball_list[0] == 1 else 1]
for i in range(1, N):
    if ball_list[i] == 1:
        R.append(R[-1] + 1)
        B.append(B[-1])
    else:
        R.append(R[-1])
        B.append(B[-1] + 1)

arr1 = [0] # R...B 왼쪽 빨강, 오른쪽 파랑
arr2 = [0] # B...R 왼쪽 파랑, 오른쪽 빨강
for i in range(1, N):
    if ball_list[i] == 1:
        arr2.append(min(arr2[i - 1], arr1[i - 1] + min(B[i - 1], R[i - 1])))
        arr1.append(min(arr2[i - 1] + min(B[i], R[i]), arr1[i - 1] + 1, B[i]))
    
    else:
        arr1.append(min(arr1[i - 1], arr2[i - 1] + min(B[i - 1], R[i - 1])))
        arr2.append(min(arr1[i - 1] + min(B[i], R[i]), arr2[i - 1] + 1, R[i]))

    _ = 1

print(min(arr1[-1], arr2[-1]))