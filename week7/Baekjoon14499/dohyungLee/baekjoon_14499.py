import sys
input = sys.stdin.readline

# 조건에 따라 입력 받기
N, M, x, y, K = map(int, input().split())
diceMap = list()

for _ in range(N) :
    diceMap.append(list(map(int, input().split())))

orderList = list(map(int, input().split()))

# 주사위 세팅
dice = [0] * 6

# 처음에 놓였을 때 밑면 세팅 (바닥면->칸 복사 경우 존재X)
dice[2] = diceMap[x][y]

# 위치에 따른 주사위 번호 지정
topDice = 0
leftDice = 4
rightDice = 5
bottomDice = 2
upDice = 3
downDice = 1

# 명령 이행
for i in orderList :
    # 동쪽으로 이동
    if i == 1 and y+1 < M :
        # 주사위 위치 변화
        topDice, leftDice, rightDice, bottomDice = leftDice, bottomDice, topDice, rightDice
        # x,y (주사위의 지도내에서 위치) 변화
        y += 1
        # 바닥면 -> 칸 복사
        if diceMap[x][y] == 0 :
            diceMap[x][y] = dice[bottomDice]
        # 칸 -> 바닥면 복사
        else :
            dice[bottomDice] = diceMap[x][y]
            diceMap[x][y] = 0
        
        # 출력    
        print(dice[topDice])
    
    # 서쪽으로 이동
    elif i == 2 and y-1 >= 0 :
        topDice, leftDice, rightDice, bottomDice = rightDice, topDice, bottomDice, leftDice
        y -= 1
        if diceMap[x][y] == 0 :
            diceMap[x][y] = dice[bottomDice]
        else :
            dice[bottomDice] = diceMap[x][y]
            diceMap[x][y] = 0
            
        print(dice[topDice])
    
    # 북쪽으로 이동
    elif i == 3 and x-1 >= 0 :
        topDice, upDice, bottomDice, downDice = downDice, topDice, upDice, bottomDice
        x -= 1
        if diceMap[x][y] == 0 :
            diceMap[x][y] = dice[bottomDice]
        else :
            dice[bottomDice] = diceMap[x][y]
            diceMap[x][y] = 0
            
        print(dice[topDice])
    
    # 남쪽으로 이동
    elif i == 4 and x+1 < N :
        topDice, upDice, bottomDice, downDice = upDice, bottomDice, downDice, topDice
        x += 1
        if diceMap[x][y] == 0 :
            diceMap[x][y] = dice[bottomDice]
        else :
            dice[bottomDice] = diceMap[x][y]
            diceMap[x][y] = 0
            
        print(dice[topDice])