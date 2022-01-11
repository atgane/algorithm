#points(list): 점 좌표의 리스트
#points[0], [1](int): 점 x, y 좌표
#N(int): 점의 개수

def convex_hull(points, N):
    points = sorted(points)
    if len(points) <= 1:
        return points
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lower = []
    upper = []
    for i in range(N):
        j = N - 1 - i
        while len(lower) >= 2 and cross(lower[-2], lower[-1], points[i]) <= 0:
            lower.pop()
        lower.append(points[i])
        while len(upper) >= 2 and cross(upper[-2], upper[-1], points[j]) <= 0:
            upper.pop()
        upper.append(points[j])
    return lower[:-1] + upper[:-1]