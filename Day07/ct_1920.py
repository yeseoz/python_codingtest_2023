# 백준 1920 - 원하는 정수 찾기
N = int(input()) # 5
A = list(map(int, input().split())) # 4 1 5 2 3
A.sort() # 파이썬 리스트에서 제공하는 기본 정렬
M = int(input())
target_list = list(map(int, input().split())) # 1 3 7 9

for i in range(M):
    find = False
    target = target_list[i]

    #이진탐색 시작
    start = 0
    end = N -1
    while start <= end:
        midi = int((start +end) / 2) # 중앙 인덱스 번호
        midv = A[midi] # 중앙에 있는 값
        if midv > target: # 오른쪽 날림
            end = midi - 1
        elif midv < target: # 왼쪽 날림.
            start = midi +1
        else: # 값 찾음
            find = True
            break
    if find:
        print(1)
    else:
        print(0)