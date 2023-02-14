# 단순 연결리스트 구현

class Node:
    def __init__(self) -> None:
        self.data = None
        self.link = None


# 전역 변수
memory = []
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

def printNodes(start):
    current = start
    if current == None:
        return
    
    print(current.data, end= ' -> ')
    while current.link != None:
        current = current.link
        if current.link == None:
            print(current.data)
        else:
            print(current.data, end =' -> ')
        
# 노드 추가

def insertNode(findData, insertData):
    global memory, pre, current, head
    
    if head.data == findData: # 첫노드 앞에 데이터를 넣겠다
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return

    current = head # current 제일 앞으로 땡겨줌
    while current.link != None: # 제일 마지막이 아닐경우
        pre = current
        current = current.link # 하나 뒤로감
        
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
    
    # current.link == None 까지 온 것
    node = Node()
    node.data = insertData
    current.link = node
    return # 없어도 됨

# 노드 삭제
def deleteNode(deleteData):
    global memory, pre, current, head

    if head.data == deleteData: # 첫번째 노드 삭제
        current = head
        head = head.link # 두번째 노드로 변경
        del(current)
        return

    current = head
    while current.link != None: # 첫번째 이외 노드 삭제
        pre = current # 모두 첫번째 노드 가리킴
        current = current.link # 두번째 노드 가리킴
        if current.data == deleteData:
            pre.link = current.link # current 가리키는 노드를 pre가 가리키도록 (삭제)
            del(current)
            return

#노드검색     
def findNode(findData):
    global memory, pre, current, head

    current = head # 첫번째 노드부터
    if current.data == findData:
        return current
    while current.link != None:
        current = current.link # 다음 노드로 넘어감
        if current.data == findData:
            return current
        
    return Node() # 없으면 빈노드 반환

if __name__ == '__main__':
    node = Node()
    node.data = dataArray[0] # 다현
    head = node # 현재 노드
    memory.append(node)

    for data in dataArray[1:]: # 두번째 노드 이후 4번 반복
        pre = node
        node = Node()
        node.data = data # 정연 쯔위 사나 지효 순
        pre.link = node
        memory.append(node) 

    printNodes(head) # 전체 출력

    print('-----노드추가-----')

    insertNode('다현', '화사') # 맨앞에 화사 노드 추가
    printNodes(head)
    insertNode('사나', '솔라') # 중간에 노드추가
    printNodes(head)
    insertNode('재남', '문별') # 맨 마지막에 노드 추가
    printNodes(head)

    print('-----노드삭제------')

    deleteNode('화사')
    printNodes(head)

    deleteNode('지효')
    printNodes(head)

    deleteNode('재남')
    printNodes(head)

    print('----노드 검색-----')
    result = findNode('정연')
    if result.data == '정연':
        print('데이터 찾았습니다..')
    else:
        print('데이터가 없습니다.')
    
    result = findNode('대남')
    print(result.data)


    