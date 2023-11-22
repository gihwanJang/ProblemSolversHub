T = int(input())
for test_case in range(1, T + 1):
    # 입력 받기
    num = list(map(int, str(input())))
    
    # 0으로 시작
    editNum = 0
    
    # 기본은 False
    defaultSetting = False
    
    # 0이 아니라면 변화 +1
    for i in num :
        if int(i) != defaultSetting :
            defaultSetting = not defaultSetting
            editNum += 1
    print(f"#{test_case} {editNum}")