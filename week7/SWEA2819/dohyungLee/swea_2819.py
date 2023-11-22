T = int(input())
 
def seekMap(x, y, grid, tmpStorage, numStorage) :
    # 입력 받기
    tmpStorage.append(str(grid[x][y]))
    if len(tmpStorage) == 7 :
        tmpInt = "".join(tmpStorage)
        numStorage.add(tmpInt)
        tmpStorage.pop()
        return numStorage, tmpStorage
     
    # 상하좌우 조사 + 백트래킹
    else :
        if x > 0 :
            numStorage, tmpStorage = seekMap(x-1, y, grid, tmpStorage, numStorage)
 
        if y > 0 :
            numStorage, tmpStorage = seekMap(x, y-1, grid, tmpStorage, numStorage)
             
        if x < 3 :
            numStorage, tmpStorage = seekMap(x+1, y, grid, tmpStorage, numStorage)
             
        if y < 3 :
            numStorage, tmpStorage = seekMap(x, y+1, grid, tmpStorage, numStorage)
 
        tmpStorage.pop()
        return numStorage, tmpStorage

for test_case in range(1, T + 1):
    grid = list()
    for _ in range(4) :
        grid.append(list(map(int, input().split())))
     
    numStorage = set()
    
    # 시작지점을 정하여 검사 시작
    for spX in range(4) :
        for spY in range(4) :
            tmpStorage = list()
            numStorage, tmpStorage = seekMap(spX, spY, grid, tmpStorage, numStorage)
             
    print(f"#{test_case} {len(numStorage)}")