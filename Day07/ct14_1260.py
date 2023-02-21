# 백준 1260 DFS와 BFS

from queue import Queue
N, M, Start = map(int, input().split())
A = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(N + 1):
    A[i].sort()

visited = [False]*(N + 1)

# DFS 함수 정의
def DFS(v):
    print(v, end=' ')
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

# BFS 함수 정의
def BFS(v):
    queue = Queue()
    queue.put(v)
    visited[v] = True
    while queue.empty != True:
        now = queue.get()
        print(now, end = ' ')
        for i in A[now]:
            if not visited[i]:
                visited[i] = True
                queue.put(i)
# DFS 실행
visited = [False]*(N + 1)
DFS(Start)
print()
# BFS 실행
visited = [False] * (N + 1)
BFS(Start)
