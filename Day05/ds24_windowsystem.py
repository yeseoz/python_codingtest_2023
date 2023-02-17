# C:\Windows\System32 파일 출력
import os

#print(dir(os)) os라는 클래스 안에 뭐가 있는지 확인
def makeFileList(foldername):
    fnameAry = []
    folderName = 'C:\Source\python_codingtest_2023'
    for _, _, fnames in os.walk(folderName): # top, dirs, nondirs  # 이렇게 써도 무방 어짜피 안쓰니까
    #for dirName, subDirList, fnames in os.walk(folderName): # top, dirs, nondirs
        for fname in fnames:
            fnameAry.append(fname)
    return fnameAry

# 삽입정렬 소스
def insertionSort(ary):
    n = len(ary)
    for end in range(1, n):
        for cur in range(end, 0, -1):
            if(ary[cur-1] < ary[cur]): # <= 내림차순 정렬
                # tmp = ary[cur-1]
                # ary[cur-1] = ary[cur]
                # ary[cur] = tmp
                ary[cur-1], ary[cur] = ary[cur], ary[cur-1] #???!! => 파이썬 swap
    return ary


fileAry = makeFileList('C:/Program Files/Common Files')
fileAry = insertionSort(fileAry)
print('파일명 역순 정렬 --> ', fileAry)
