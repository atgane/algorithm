import sys
ssr = sys.stdin.readline

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def cross_check(line1, line2):
    a1 = cross(line1[0], line1[1], line2[0])
    a2 = cross(line1[0], line1[1], line2[1])
    a3 = cross(line2[0], line2[1], line1[0])
    a4 = cross(line2[0], line2[1], line1[1])
    ans = 0
    if a1 * a2 <= 0 and a3 * a4 <= 0:
        if a1 * a2 == 0 and a3 * a4 == 0:
            if min(line1[0][0], line1[1][0]) <= max(line2[0][0], line2[1][0]) and min(line1[0][1], line1[1][1]) <= max(line2[0][1], line2[1][1]) \
                and min(line2[0][0], line2[1][0]) <= max(line1[0][0], line1[1][0]) and min(line2[0][1], line2[1][1]) <= max(line1[0][1], line1[1][1]):
                ans = 1
        else:
            ans = 1
    return ans

a1, a2, a3, a4 = map(int, ssr().split())
line1 = [[a1, a2], [a3, a4]]
b1, b2, b3, b4 = map(int, ssr().split())
line2 = [[b1, b2], [b3, b4]]
print(cross_check(line1, line2))