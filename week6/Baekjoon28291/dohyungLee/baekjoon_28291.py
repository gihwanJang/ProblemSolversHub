def main() :
    # 맵의 가로 세로 및 회로 블록의 개수 입력
    W, H = map(int, input().split())
    N = int(input())

    # W*H 크기의 사각형 맵
    xyList = [[None]*W for _ in range(H)]
    
    # 레드스톤 블록의 좌표(x,y) 기록
    blockXList = list()
    blockYList = list()
    
    # 램프의 개수
    lampNum = 0

    # 레드스톤의 종류에 따라 맵에 생성
    for _ in range(N) :
        r, x, y = input().split()
        
        # 레드스톤 블록이면 양쪽에 15의 신호를 전달해야하므로 16
        if r == "redstone_block" :
            xyList[int(y)][int(x)] = 16
            blockXList.append(int(x))
            blockYList.append(int(y))
        
        # 레드스톤 가루 
        elif r == "redstone_dust" :
            xyList[int(y)][int(x)] = 0
        else :
            xyList[int(y)][int(x)] = -1
            lampNum += 1
    
    # 레드스톤 신호가 램프로 전달되는지 확인
    result = redstone(W, H, xyList, blockXList, blockYList, lampNum)
    
    # 결과에 따라 성공/실패 요구 확인
    if result :
        print("success")
    else :
        print("failed") 

# 신호를 상하좌우로 전달하는 함수
def spreadLight(xyList, x, y, W, H, lamps) :
    
    # 좌로 전달
    if x > 0 and type(xyList[y][x-1]) is int :
        # 만약 왼쪽에 있는데 램프라면 불을 키고 램프의 수 변경
        if xyList[y][x-1] == -1 and xyList[y][x] != 1:
            lamps += 1
            xyList[y][x-1] = -2
        # 가루라면 그곳에 신호를 보내고 신호 상하좌우 전달
        elif xyList[y][x-1] >= 0 and xyList[y][x-1] < xyList[y][x] :
            xyList[y][x-1] = xyList[y][x] - 1
            if xyList[y][x-1] > 0 :
                xyList, lamps = spreadLight(xyList, x-1, y, W, H, lamps)

    # 하로 전달 (이하 같다)
    if y > 0 and type(xyList[y-1][x]) is int :
        if xyList[y-1][x] == -1 and xyList[y][x] != 1:
            lamps += 1
            xyList[y-1][x] = -2
        
        elif xyList[y-1][x] >= 0 and xyList[y-1][x] < xyList[y][x] :
            xyList[y-1][x] = xyList[y][x] - 1
            if xyList[y-1][x] > 0 :
                xyList, lamps = spreadLight(xyList, x, y-1, W, H, lamps)

    # 우로 전달 (이하 같다)
    if x < W - 1 and type(xyList[y][x+1]) is int :
        if xyList[y][x+1] == -1 and xyList[y][x] != 1:
            lamps += 1
            xyList[y][x+1] = -2

        elif xyList[y][x+1] >= 0 and xyList[y][x+1] < xyList[y][x] :
            xyList[y][x+1] = xyList[y][x] - 1
            if xyList[y][x+1] > 0 :
                xyList, lamps = spreadLight(xyList, x+1, y, W, H, lamps)

    # 상으로 전달 (이하 같다)
    if y < H - 1 and type(xyList[y+1][x]) is int :
        if xyList[y+1][x] == -1 and xyList[y][x] != 1:
            lamps += 1
            xyList[y+1][x] = -2

        elif xyList[y+1][x] >= 0 and xyList[y+1][x] < xyList[y][x] :
            xyList[y+1][x] = xyList[y][x] - 1
            if xyList[y+1][x] > 0 :
                xyList, lamps = spreadLight(xyList, x, y+1, W, H, lamps)

    return xyList, lamps                                  
     
# 레드스톤 회로 신호를 찾는 함수   
def redstone(W, H, xyList, blockX, blockY, lampNum) :
    # 초기에 램프의 개수 세팅
    lamps = 0
    # 레드스톤 블록의 위치부터 신호 전달
    for x, y in zip(blockX, blockY) :
        xyList, lamps = spreadLight(xyList, x, y, W, H, lamps)
    
    # 만약 신호 전달이 끝난 함수에서 램프가 있다면 False
    for x in range(W) :
        for y in range(H) :
            if xyList[y][x] == -1 :
                return False
            
    # 찾은 램프의 개수가 초기 램프와 같다면 True
    if lamps == lampNum :
        return True
    else :
        return False
                        
if __name__ == "__main__" :
    main()