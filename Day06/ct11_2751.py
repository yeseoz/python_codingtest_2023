# 백준 2751 - 수정렬하기2
# 1000000000000 1조개 처리 O(n^2)은 불가
import sys
input = sys.stdin.readline
print = sys.stdout.write

A = []
tmp = []

def merge_sort(s, e):  # 병합정렬
    if e - s < 1: return
    m = s + (e - s) // 2
    merge_sort(s, m)
    merge_sort(m + 1, e)

    for i in range(s, e+1):
        tmp[i] = A[i]
    k = s
    index1 = s
    index2 = m+1
    while index1 <= m and index2 <= e:  # 두 그룹을 병합
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1
    while index1 <= m: 
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= e:
        A[k] = tmp[index2]
        k += 1
        index2 += 1

N = int(input())
A = [0] * int(N + 1)
tmp = [0] * int(N+1)

for i in range(1, N+1):
    A[i] = int(input())

merge_sort(1, N)

for i in range(1, N+1):
    print(str(A[i]) + '\n')
