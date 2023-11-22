T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # 숫자와 교환 횟수 입력
    num, changeLimit = input().split()
    changeLimit = int(changeLimit)
    numLen = len(num)
    k = 0
    i = 0
    
    # 같은 숫자일 때를 대비하여 필요한 함수
    sameNumCheck = False
    sameNumIndex1 = -1
    sameNumIndex2 = -1
    changedIndexList = [[] for _ in range(10)]

    # 교환횟수에 도덜하면 반복문 탈출     
    while i != changeLimit :
        
        # 모든 숫자 사이 정렬이 끝났을 때
        if k == numLen :
 
            # 만약 같은 숫자가 있다면 같은 숫자끼리 교환 반복
            if sameNumCheck == False :
                for a in range(numLen-1) :
                    for b in range(a+1, numLen) :
                        if num[a] == num[b] :
                            sameNumIndex1 = a
                            sameNumIndex2 = b
                            sameNumCheck = True
                            break

            # 만약 숫자가 같지 않다면 일의 자리와 십의 자리 교체
            num = list(num)
            if sameNumIndex1 == -1 :
                num[numLen-1], num[numLen-2] = num[numLen-2], num[numLen-1]
            
            # 같은 숫자 교환반복
            else :
                num[sameNumIndex1], num[sameNumIndex2] = num[sameNumIndex2], num[sameNumIndex1]
 
            # 다시 숫자로 합치기
            num = ''.join(num)
            i += 1
        
        # 정렬
        else :
            maxNum = 0
            maxIndex = -1
 
            # 가장 높은 자리 숫자를 가장 높은 숫자와 교환
            for j in range(1, numLen-k) :
                if int(num[j+k]) >= maxNum :
                    maxNum = int(num[j+k])
                    maxIndex = j+k
            if maxIndex != -1 :
                if num[k] < num[maxIndex] :
                    num = list(num)
                    num[k] , num[maxIndex] = num[maxIndex], num[k]
 
                    # 교환에 관여한 같은 숫자들 끼리는 교환된 숫자 사이 자리 교환 가능
                    changedIndexList[int(num[k])].append(maxIndex)
                    i += 1
                    for idxNum in range(10) :
                        changedIndexList[idxNum].sort()
                        for idx1 in range(len(changedIndexList[idxNum])-1) :
                            for idx2 in range(idx1+1, len(changedIndexList[idxNum])) :
                                if num[changedIndexList[idxNum][idx1]] < num[changedIndexList[idxNum][idx2]] :
                                    num[changedIndexList[idxNum][idx1]], num[changedIndexList[idxNum][idx2]] = num[changedIndexList[idxNum][idx2]], num[changedIndexList[idxNum][idx1]]
                    num = ''.join(num)
 
            k += 1
    print(f"#{test_case} {num}")
    # ///////////////////////////////////////////////////////////////////////////////////