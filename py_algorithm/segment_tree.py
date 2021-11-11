# arr(list): 수열
# tree(list): segment tree. N log N 크기 배열
# node(int): 시작은 1로
# start(int), end(int): 배열 처음, 끝
# right(int), left(int): 왼쪽, 오른쪽 구간 
# index(int), diff(int): 갱신할 쿼리의 번호와 차이

def init(arr, tree, node, start, end):
    if start == end: 
        tree[node] = arr[start]
    else:
        tree[node] = init(arr, tree, node * 2, start, (start + end) // 2) + init(arr, tree, node * 2 + 1, (start + end) // 2 + 1, end)
    return tree[node]

def func(tree, node, start, end, left, right):
    if left > end or right < start: return 0
    if left <= start and right >= end: return tree[node]
    return func(tree, node * 2, start, (start + end) // 2, left, right) + func(tree, node * 2 + 1, (start + end) // 2 + 1, end, left, right)

def update(tree, node, start, end, index, diff):
    if (index < start or index > end): return
    tree[node] = tree[node] + diff
    if start != end:
        update(tree, node * 2, start, (start + end) // 2, index, diff)
        update(tree, node * 2 + 1, (start + end) // 2 + 1, end, index, diff)
