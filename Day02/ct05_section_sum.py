# 2차원 구간합
# 백준 - 11660

import sys
input = sys.stdin.readline

n, m = tuple(map(int, input().split())) # 2차원 행렬크기, 질의갯수
A = [[0] * (n+1)]
D = [[0] * (n+1) for _ in range(n + 1)] # for_ 는 아무것도 안하는거임
# 인덱스 1,2,3, 이렇게 시작하니까 [0] 은 안쓰는거임

# 2차원 배열 만듦
for i in range(n):
    rows = list(map(int, input().split()))
    A_row = [0] + rows
    A.append(A_row)

# 2차원 합배열 D 만듬 0 (1024x1024) 백만
for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j] 

# 구간합
for _ in range(m): # m=3 일때 _ => m 값을 쓰지 않겠다
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)