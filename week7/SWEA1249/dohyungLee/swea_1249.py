T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # 입력
    N = int(input())
    mapList = list()
     
    for _ in range(N) :
        mapList.append(list(map(int, str(input()))))
    
    # 전체를 무한으로 채우되, 제일 마지막 칸은 0 
    mapStorage = [[float("inf")]* N for _ in range(N)]
    mapStorage[N-1][N-1] = 0
 
    changed = True
 
    # 바뀐게 없을 때까지 최소 값을 찾아 동서남북 검사 후 백트래킹
    # 이 때 (N-1, N-1) ~ (0, 0)까지
    while changed == True :
        changed = False
        for y in range(N-1, -1, -1) :
            for x in range(N-1, -1, -1) :
                if x < N-1 :
                    if mapStorage[y][x+1] > mapStorage[y][x] + mapList[y][x+1] :
                        mapStorage[y][x+1] = mapStorage[y][x] + mapList[y][x+1]
                        changed = True
                if y < N-1 :
                    if mapStorage[y+1][x] > mapStorage[y][x] + mapList[y+1][x] :
                        mapStorage[y+1][x] = mapStorage[y][x] + mapList[y+1][x]
                        changed = True
                if y > 0 :
                    if mapStorage[y-1][x] > mapStorage[y][x] + mapList[y-1][x] :
                        mapStorage[y-1][x] = mapStorage[y][x] + mapList[y-1][x]
                        changed = True
                if x > 0 :
                    if mapStorage[y][x-1] > mapStorage[y][x] + mapList[y][x-1] :
                        mapStorage[y][x-1] = mapStorage[y][x] + mapList[y][x-1]
                        changed = True
 
    # (0,0)에서 최소값이 경로의 최소 복구 시간
    print(f"#{test_case} {mapStorage[0][0]}")                
    # ///////////////////////////////////////////////////////////////////////////////////
