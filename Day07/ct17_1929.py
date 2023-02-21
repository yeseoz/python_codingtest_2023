# 백준 1929 - 소수구하기
import math
M, N = map(int, input().split()) # 3 16
A = [0] * (N + 1) # 초기화
#print(A)

for i in range(2, N + 1):
    A[i] = i # 인덱스 채워넣기

for i in range(2, int(math.sqrt(N))+1): # 제곱근 까지만 수행
    if A[i] == 0:
        continue
    # i == 2 일때 4부터 시작해서 4,6,8,...,16
    # i == 3 일때 6부터 시작해서 6,9,...,15
    for j in range(i + i, N + 1, i): # 배수로 지우기
        A[j] = 0 # 소수가 아닌건 지우기

for i in range(M, N + 1):
    if A[i] != 0:
        print(A[i])
    