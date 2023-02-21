# 백준 11047 - 동전개수최솟값
N, K = map(int, input().split()) # 10 4750
A = [0] * N

for i in range(N):
    A[i] = int(input())

A.sort()

count = 0

for i in range(N-1, -1, -1): # 역순으로
    if A[i] <= K: # 현재의 동전의 가치가 K보다 작거나 같으면
        count += K // A[i]
        K = K % A[i] # 현재 동전 나머지를 금액으로 업데이트

print(count)