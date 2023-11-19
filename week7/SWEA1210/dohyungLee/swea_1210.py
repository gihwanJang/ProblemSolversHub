for tc in range(10):
    
    # 입력 받기 + 미로 생성
    test_case = int(input())
    maze = list()
    for _ in range(100) :
        maze.append(list(map(int, input().split())))
    
    # 초기 위치 (출구) 세팅
    for x in range(100) :
        if maze[99][x] == 2 :
            xLocation = x
            break
    yLocation = 99
     
    # 네방향으로 탐색
    direction = "up"
    while direction != "goal" :
        if direction == "up" : 
            if yLocation == 0 :
                print(f"#{test_case} {xLocation}")
                direction = "goal"
            if xLocation > 0 and maze[yLocation][xLocation-1] == 1 :
                xLocation -= 1
                direction = "left"
            elif xLocation < 99 and maze[yLocation][xLocation+1] == 1 :
                xLocation += 1
                direction = "right"
            else :
                yLocation -= 1
        elif direction == "left" : 
            if xLocation > 0 and maze[yLocation][xLocation-1] == 1 :
                xLocation -= 1
            else :
                yLocation -= 1
                direction = "up"
        elif direction == "right" : 
            if xLocation < 99 and maze[yLocation][xLocation+1] == 1 :
                xLocation += 1
            else :
                yLocation -= 1
                direction = "up"