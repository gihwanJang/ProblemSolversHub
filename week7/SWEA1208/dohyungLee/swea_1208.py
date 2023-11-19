# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    
    # 가로 길이 및 상자의 높이 입력
    dumpLimit = int(input())
    boxList = list(map(int, input().split()))
    
    # 최대와 최소 값을 찾은 다음
    for _ in range(dumpLimit) :
        mx = max(boxList)
        mn = min(boxList)
        diff = mx - mn
        
        # 최대-최소 차가 1보다 작다면 출력
        if diff <= 1 :
            print(f"#{test_case} {diff}")
            break
        
        # 아니라면 최대 1 빼주고, 최소 1 더해준다
        else :
            boxList[boxList.index(mx)] -= 1
            boxList[boxList.index(mn)] += 1
    
    # 최대-최소 차를 다 변경해도 1보다 크다면 이대로 출력
    mx = max(boxList)
    mn = min(boxList)
    diff = mx - mn
    print(f"#{test_case} {diff}")
    