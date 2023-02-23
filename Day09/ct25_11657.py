# 백준 11657 - 타임머신
import sys
N, M = map(int, input().split())
edges = []
distance = [sys.maxsize] * (N + 1)

for _ in range(M):
    start, end, time = map(int, input().split())
    edges.append((start, end, time))

# 벨만 포드 수행
distance[1] = 0

for _ in range(N - 1):
    for start, end, time in edges:
        if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
            distance[end] = distance[start] + time

# 음수 사이클 확인
myCycle = False

for start, end, time in edges:
    if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
        myCycle = True # 음수 사이클이 존재
        break # 음수사이클이 있으면 더이상 진행할 필요 없음

if not myCycle:
    for i in range(2, N + 1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else: # 도시에 방문안함
            print(-1)
else:
    print(-1)