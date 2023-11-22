T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    sum = 0
    
    for i in range(N) :
        numLine = input()
        # 반 미만일 때는 1, 3, .. 순으로 더해주기
        if i < N/2 :
            for j in range(int((N-1)/2-i), int((N-1)/2+i+1)) :
                sum += int(numLine[j])
        # 반 이상일 때는 (N+1)-2, ..., 3, 1 순으로 더해주기
        else :
            for j in range(int((N-1)/2-N+i+1), int((N-1)/2+N-i)) :
                sum += int(numLine[j])
    print(f"#{test_case} {sum}")