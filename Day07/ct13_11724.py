# 백준 11724 연결요소의 개수
import sys
# 파이썬에는 재귀호출 제한이 있음 1000번까지 / 1000번이 넘으면 종료시켜버림(기본)
sys.setrecursionlimit(10 ** 6) # 천개 넘게 쓰려고 1000000
# 입력받는 속도가 느리기 때문에, 백준에서 그냥 돌리면 입력오류 발생가능
input = sys.stdin.readline

n, m = map(int, input().split()) # 노드 개수, 엣지
A = [[] for _ in range(n + 1)] # 초기화 x, 7열로 된 2차원 배열 리스트
visited = [False] * (n+1) # [0, 1, 2, 3, 4, 5, 6]

# DFS 함수
def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]: # 방문을 안했다면
            DFS(i)

for _ in range(m): # 에지 개수만큼
    s, e = map(int, input().split())
    A[s].append(e) # 무방향이기때문에 양쪽 에지 추가
    A[e].append(s)

count = 0

for i in range(1, n+1):
    if not visited[i]:
        count+=1
        DFS(i)

print(count)

