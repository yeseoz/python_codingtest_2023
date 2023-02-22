# 백준 18352 - 특정거리도시찾기
import sys
from collections import deque
input = sys.stdin.readline # 입력속도를 빠르게!

N, M, K, X = map(int, input().split()) # 노드수, 에지수, 목표거리, 시작노드
A = [[] for _ in range(N + 1)] # 초기화
answer = []
visited = [-1] * (N + 1) # -1로 초기화 하고 N+1 개 만듬

def BFS(v):
    q = deque()
    q.append(v)
    visited[v] += 1 # v번째에다가 +1 => 0 올 바뀜
    while q:
        now = q.popleft() # 왼쪽에서 들어온 것부터 빠진다?
        for i in A[now]:
            if visited[i] == -1: # 미방문이면
                visited[i] = visited[now]+1 # 0
                q.append(i)

# 두번째 줄 부터 엣지 입력
for _ in range(M):
    S, E = map(int, input().split())
    A[S].append(E)

BFS(X) # 시작점 부터 BFS시작

for i in range(N + 1):
    if visited[i] == K:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)