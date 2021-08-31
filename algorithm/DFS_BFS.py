# _data(list): 정점이 다른 정점과 연결된 정보를 담은 리스트를 원소로 하는 리스트
# _data[1](list): 1번 정점이 다른 정점과 연결된 정보를 담은 리스트(0번은 무시)
# ex) _data[1] = [3, 4, 5]이면 1번 정점이 3, 4, 5번 정점과 연결되어 있다는 의미
# _start(int): 시작 정점
# return: DFS, BFS가 방문한 순서의 정점 리스트

from collections import deque

def DFS(_data, _start):
    visited = []
    stack = []
    stack.append(_start)
    while True:
        tmp_node = stack.pop()
        child_list = _data[tmp_node]
        child_list.reverse()
        for i in child_list:
            if i not in visited:
                if i in stack:
                    del stack[stack.index(i)]
                stack.append(i)
        visited.append(tmp_node)
        if stack == []:
            break
    return visited
    
def BFS(_data, _start):
    visited = []
    queue = deque([])
    queue.append(_start)
    while True:
        tmp_node = queue.popleft()
        child_list = _data[tmp_node]
        child_list.reverse()
        for i in child_list:
            if not (i in visited or i in queue):
                queue.append(i)
        visited.append(tmp_node)
        if len(queue) == 0:
            break
    return visited