# 백준 1541 - 잃어버린 괄호

answer = 0
A =list(map(str, input().split("-"))) # - 를 기준으로 자른 것을 문자열로 리스트를 만듬

def mySum(i): # - 로 나눈 각 수식 문자열 합구하기 함수
    result = 0
    temp = str(i).split("+") # + 기준으로 수식을 자름 78+45
    for k in temp:
        result += int(k) # '78' 같은 문자열이므로 int()형으로 변환

    return result


for s in range(len(A)):
    temp = mySum(A[s])
    if s == 0:
        answer += temp # 맨 처음
    else:
        answer -= temp 

print(answer)