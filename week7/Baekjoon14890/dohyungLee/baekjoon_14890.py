import sys
input = sys.stdin.readline

# 입력 받기
N, L = map(int, input().split())

roadMap = list()

for _ in range(N) :
    roadMap.append(list(map(int, input().split())))

# 연결된 도로
connectedRoad = 0

# 가로 방향 (horizontal) 먼저 비교
for m in range(N) :
    
    # 만약 한 줄이 모두 같다면 그대로 +1
    if max(roadMap[m]) == min(roadMap[m]) :
        connectedRoad += 1
        continue
    
    # 이어진 선
    inRow = 0
    
    # 아래로 내려갔는지 표시
    down = False
    
    # 반복이 중단되었는지 표시
    breaked = False
    
    # 0~N-1번까지 [i][i+1] 비교
    for n in range(N-1) :
        
        # 차이가 2이상 나면 반복문 탈출
        if abs(roadMap[m][n]-roadMap[m][n+1]) > 1 :
            breaked = True
            break
        
        # 앞에가 1만큼 크면
        elif roadMap[m][n] > roadMap[m][n+1] :
            # 전에 블럭과 연속되었으므로 +1
            inRow += 1
            
            # 만약 아래로 내려간 상태였다면 경사로가 들어갈 수 있는지 체크
            if down is True :
                if inRow < L :
                    breaked = True
                    break
                
            # 연속 초기화, 아래로 내려갔다고 표시
            inRow = 0
            down = True
            
        # 뒤에가 1만큼 크면
        elif roadMap[m][n] < roadMap[m][n+1] :
            # 전에 블럭과 연속되었으므로 +1
            inRow += 1
            
            # 만약 아래로 내려간 상태라면
            if down is True :
                # 경사로 2개가 들어갈 수 있는지 체크
                if inRow < 2*L :
                    breaked = True
                    break
                
            # 아래로 내려간 상태가 아니라면 경사로 1개가 들어갈 수 있는지 체크
            else :
                if inRow < L :
                    breaked = True
                    break
                
            # 연속 초기화, 아래로 내려갔던 표시 해제
            inRow = 0
            down = False
            
        # 앞뒤 블럭의 크기가 같다면 연속 +1
        else :
            inRow += 1
    
    # 마지막에도 연속 +1
    inRow += 1
    
    # 중간에 반복문 탈출했으면 +0
    if breaked is False :
        # 내려간 상태라면 경사로 1개가 들어갈지 체크
        if down is True :
            if inRow >= L :
                connectedRoad += 1
        
        # 내려간 상태가 아니라면 항상 통과
        else :
            connectedRoad += 1    

# 세로 방향 (vertical) 검사 [가로 방향과 동일]
for m in range(N) :    
    inRow = 0
    down = False
    breaked = False
    for n in range(N-1) :
        if abs(roadMap[n][m]-roadMap[n+1][m]) > 1 :
            breaked = True
            break
        elif roadMap[n][m] > roadMap[n+1][m] :
            inRow += 1
            if down is True :
                if inRow < L :
                    breaked = True
                    break
            inRow = 0
            down = True
        elif roadMap[n][m] < roadMap[n+1][m] :
            inRow += 1
            if down is True :
                if inRow < 2*L :
                    breaked = True
                    break
            else :
                if inRow < L :
                    breaked = True
                    break
            inRow = 0
            down = False
        else :
            inRow += 1
    inRow += 1 
    if breaked is False :
        if down is True :
            if inRow >= L :
                connectedRoad += 1
        else :
            connectedRoad += 1  
        
print(connectedRoad)