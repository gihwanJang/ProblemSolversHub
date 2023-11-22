import sys
input = sys.stdin.readline

# 입력 받기
wheelList = list()

for _ in range(4) :
    wheelList.append(list(input().rstrip('\n')))

wheelHead = [0,0,0,0]
tmpHead = [0,0,0,0]

K = int(input())

# 왼쪽에 있는 바퀴와 비교
def effectLeft(wheelNum, clockwise) :
    # Index 범위를 벗어나는 것을 방지하기 위한 계산
    leftWheel = (wheelNum-1) % 4
    rightWheel = (wheelNum-2) % 4
    leftNum = (wheelHead[leftWheel]-2) % 8
    rightNum = (wheelHead[rightWheel]+2) % 8
    
    # 왼쪽에 있는 톱니바퀴 맞닿은 부분과 비교
    if wheelList[leftWheel][leftNum] != wheelList[rightWheel][rightNum] :
        # 회전 조건에 충족되면 왼쪽에 반대방향으로 
        if clockwise == 1 :
            tmpHead[rightWheel] += 1
            return wheelNum - 1, -1
        else :
            tmpHead[rightWheel] -= 1
            return wheelNum - 1, 1
    return wheelNum - 1, 0
        
# 오른쪽에 있는 바퀴와 비교
def effectRight(wheelNum, clockwise) :
    # Index 범위를 벗어나는 것을 방지하기 위한 계산
    leftWheel = (wheelNum-1) % 4
    leftNum = (wheelHead[leftWheel]+2) % 8
    rightNum = (wheelHead[wheelNum]-2) % 8
    
    # 오른쪽에 있는 톱니바퀴 맞닿은 부분과 비교
    if wheelList[leftWheel][leftNum] != wheelList[wheelNum][rightNum] :
        # 회전 조건에 충족되면 오른쪽에 반대방향으로
        if clockwise == 1 :
            tmpHead[wheelNum] += 1
            return wheelNum+1, -1
        else :
            tmpHead[wheelNum] -= 1
            return wheelNum+1, 1 
    return wheelNum+1, 0

# K번 반복
for _ in range(K) :
    # 바퀴 번호와 시계 방향 입력 받음
    wheelNum, clockwise = map(int, input().split())
    
    # 시계 방향으로 임시 Head 수정
    tmpHead[wheelNum-1] -= clockwise
    
    # 1번 바퀴는 2, 3, 4번 순으로 끊길 때 까지 검사
    if wheelNum == 1 :
        while clockwise != 0 and wheelNum < 4:
            wheelNum, clockwise = effectRight(wheelNum, clockwise)
            
    # 2번 바퀴는 1번에 영향 후 3, 4번 순으로 끊길 때 까지 검사
    elif wheelNum == 2 :
        _, __ = effectLeft(wheelNum, clockwise)
        while clockwise != 0 and wheelNum < 4 :
            wheelNum, clockwise = effectRight(wheelNum, clockwise)
            
    # 3번 바퀴는 4번에 영향 후 2, 1번 순으로 끊길 때 까지 검사
    elif wheelNum == 3 :
        _, __ = effectRight(wheelNum, clockwise)
        while clockwise != 0 and wheelNum > 1 :
            wheelNum, clockwise = effectLeft(wheelNum, clockwise)
    
    # 4번 바퀴는 3, 2, 1번 순으로 끊길 때 까지 검사
    else :
        while clockwise != 0 and wheelNum > 1 :
            wheelNum, clockwise = effectLeft(wheelNum, clockwise)
            
    wheelHead = tmpHead.copy()

points = 0

# 톱니바퀴에 따라 점수 더해주기
for i in range(4) :
    headNum = wheelHead[i] % 8
    if wheelList[i][headNum] == '1' :
        points += 2**i

print(points)