import sys
ssr = sys.stdin.readline

def cross_product(ux, uy, vx, vy):
    t = ux * vy - vx * uy
    if t > 0: return 1
    if t < 0: return -1
    return 0

a = []
a.extend(list(map(int, ssr().split())))
a.extend(list(map(int, ssr().split())))

a1 = cross_product(a[0] - a[2], a[1] - a[3], a[2] - a[4], a[3] - a[5])
a2 = cross_product(a[0] - a[2], a[1] - a[3], a[2] - a[6], a[3] - a[7])
a3 = cross_product(a[4] - a[6], a[5] - a[7], a[6] - a[0], a[7] - a[1])
a4 = cross_product(a[4] - a[6], a[5] - a[7], a[6] - a[2], a[7] - a[3])

ans = 0
if a1 * a2 <= 0 and a3 * a4 <= 0:
    if a1 * a2 == 0 and a3 * a4 == 0:
        if min(a[0], a[2]) <= max(a[4], a[6]) and min(a[1], a[3]) <= max(a[5], a[7]) and min(a[4], a[6]) <= max(a[0], a[2]) and min(a[5], a[7]) <= max(a[1], a[3]):
            ans = 1
    else:
        ans = 1
print(ans)