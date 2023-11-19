for test_Case in range(1, 11) :
    # 조망권이 주어진 집
    goodViewHouses = 0
    
    # 건물의 개수와 건물의 높이 입력
    N = int(input())
    buildingFloors = list(map(int, input().split()))
     
    # 0, 1번째 일 때는 각각 오른쪽 2개, 왼쪽 1개-오른쪽 2개 일 때만 고려 
    if buildingFloors[0] > buildingFloors[1] and buildingFloors[0] > buildingFloors[2] :
        goodViewHouses += buildingFloors[0] - max(buildingFloors[1], buildingFloors[2])
    if buildingFloors[1] > buildingFloors[0] and buildingFloors[1] > buildingFloors[2] and buildingFloors[1] > buildingFloors[3] :
        goodViewHouses += buildingFloors[1] - max(buildingFloors[0], buildingFloors[2], buildingFloors[3])
    
    # 2~N-3 번째 일 때는 양쪽 2개 고려
    for i in range(2, N-2) :
        if buildingFloors[i] > buildingFloors[i-1] and buildingFloors[i] > buildingFloors[i-2] and buildingFloors[i] > buildingFloors[i+1] and buildingFloors[i] > buildingFloors[i+2] :
            goodViewHouses += buildingFloors[i] - max(buildingFloors[i-1], buildingFloors[i-2], buildingFloors[i+1], buildingFloors[i+2])
    
    # N-2, N-1번째 일 때는 각각 왼쪽 2개, 오른쪽 1개-왼쪽 2개 일 때만 고려
    if buildingFloors[N-1] > buildingFloors[N-2] and buildingFloors[N-1] > buildingFloors[N-3] :
        goodViewHouses += buildingFloors[N-1] - max(buildingFloors[N-2], buildingFloors[N-3])
    if buildingFloors[N-2] > buildingFloors[N-1] and buildingFloors[N-2] > buildingFloors[N-3] and buildingFloors[N-2] > buildingFloors[N-4] :
        goodViewHouses += buildingFloors[N-2] - max(buildingFloors[N-1], buildingFloors[N-3], buildingFloors[N-4])
    print(f"#{test_Case} {goodViewHouses}")