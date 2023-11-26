def solution(places):
    answer = []
    
    # places 개수 만큼 반복
    for i in range(len(places)) :
        
        # 한번이라도 걸리면 바로 탈출
        breakpoint = False
        
        # 전체 탐지
        for y in range(5) :
            for x in range(5) :
                
                # 사람일 때 상하좌우 체크
                if places[i][y][x] == 'P' :
                    if checkLeft(x,y,places[i]) is False :
                        # 한번이라도 걸리면 breakpoing로 이중반복 탈출
                        breakpoint = True
                        break
                    if checkRight(x,y,places[i]) is False :
                        breakpoint = True
                        break
                    if checkUp(x,y,places[i]) is False :
                        breakpoint = True
                        break
                    if checkDown(x,y,places[i]) is False :
                        breakpoint = True
                        break
            if breakpoint is True :
                break

        if breakpoint is True :
            answer.append(0)
        else :
            answer.append(1)
    return answer

# 왼쪽 검사
def checkLeft(x, y, places) :
    # x가 0보다 크다면
    if x > 0 :
        
        # 사람끼리 두명이 곂치면 False
        if places[y][x-1] == 'P' :
            return False
        
        # 책상이 있다면
        elif places[y][x-1] == 'O' :
            
            # 왼쪽, 좌상하단 모두 검사 한 후 사람이 있다면 False
            if x > 1 :
                if places[y][x-2] == 'P' :
                    return False
            if y > 0 :
                if places[y-1][x-1] == 'P' :
                    return False
            if y < 4 :
                if places[y+1][x-1] == 'P' :
                    return False
                
    # 검사 통과 + 파티션이라면 True
    return True

# 상단 검사
def checkUp(x, y, places) :
    if y > 0 :
        if places[y-1][x] == 'P' :
            return False
        elif places[y-1][x] == 'O' :
            if y > 1 :
                if places[y-2][x] == 'P' :
                    return False
            if x > 0 :
                if places[y-1][x-1] == 'P' :
                    return False
            if x < 4 :
                if places[y-1][x+1] == 'P' :
                    return False
    return True

# 오른쪽 검사
def checkRight(x, y, places) :
    if x < 4 :
        if places[y][x+1] == 'P' :
            return False
        elif places[y][x+1] == 'O' :
            if x < 3 :
                if places[y][x+2] == 'P' :
                    return False
            if y > 0 :
                if places[y-1][x+1] == 'P' :
                    return False
            if y < 4 :
                if places[y+1][x+1] == 'P' :
                    return False
    return True

# 하단 검사
def checkDown(x, y, places) :
    if y < 4 :
        if places[y+1][x] == 'P' :
            return False
        elif places[y+1][x] == 'O' :
            if y < 3 :
                if places[y+2][x] == 'P' :
                    return False
            if x > 0 :
                if places[y+1][x-1] == 'P' :
                    return False
            if x < 4 :
                if places[y+1][x+1] == 'P' :
                    return False
            
    return True