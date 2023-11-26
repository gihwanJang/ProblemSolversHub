# 전체 더하기 수행
def plusRotate(idxList, nL) :
    for m in idxList :
        n1 = nL[m]
        n2 = nL[m+1]
        k = m
        while n1 == None :
            k -= 1
            n1 = nL[k]
        nL[k] = n1 + n2
        nL[m+1] = None
    return nL

# 전체 빼기 수행
def minusRotate(idxList, nL) :
    for m in idxList :
        n1 = nL[m]
        n2 = nL[m+1]
        k = m
        while n1 == None :
            k -= 1
            n1 = nL[k]
        nL[k] = n1 - n2
        nL[m+1] = None
    return nL

# 전체 곱하기 수행
def multipleRotate(idxList, nL) :
    for m in idxList :
        n1 = nL[m]
        n2 = nL[m+1]
        k = m
        while n1 == None:
            k -= 1
            n1 = nL[k]
        nL[k] = n1 * n2
        nL[m+1] = None
    return nL            

def solution(expression):
    answer = 0
    
    # 숫자의 개수
    numIdx = 0
    
    # 사칙연산 기호 개수
    expIdx = 0
    
    # 숫자를 저장할 배열
    numList = [""]
    
    # 사칙연산의 기호를 저장할 개수
    plusIdx = list()
    minusIdx = list()
    multipleIdx = list()
    
    # 숫자와 기호로 나누기
    for i in range(len(expression)) :
        # 덧셈이라면
        if expression[i] == '+' :
            # 덧셈기호 위치를 저장
            plusIdx.append(expIdx)
            
            # 기호 위치 업데이트
            expIdx += 1
            
            # 이전에 배열에 저장된 숫자 string을 int로 변환
            numList[numIdx] = int(numList[numIdx])
            
            # 그 다음 숫자 string을 저장할 배열 불러오기
            numList.append("")
            
            # 숫자 배열 위치 +1
            numIdx += 1
            
        # 뺄셈이라면 덧셈과 같이 수행
        elif expression[i] == '-' :
            minusIdx.append(expIdx)
            expIdx += 1
            numList[numIdx] = int(numList[numIdx])
            numList.append("")
            numIdx += 1
            
        # 나눗셈이라면
        elif expression[i] == '*' :
            multipleIdx.append(expIdx)
            expIdx += 1
            numList[numIdx] = int(numList[numIdx])
            numList.append("")
            numIdx += 1
        
        # 숫자라면 숫자 배열에 string으로 저장
        else :
            numList[numIdx] += expression[i]

    # 마지막에 저장된 숫자 string을 int로 변환
    numList[numIdx] = int(numList[numIdx])
           
    # 덧셈이 없다면 
    if len(plusIdx) == 0 :
        # (덧셈과) 뺄셈이 없다면
        if len(minusIdx) == 0 :
            # 곱셈만 수행
            answer = 1
            for m in numList :
                answer *= m
                
        # (덧셈과) 곱셈이 없다면
        elif len(multipleIdx) == 0 :
            # 뺄셈만 수행
            answer = numList[0]
            for m in numList[1:] :
                answer -= m
            answer = abs(answer)
            
        # 덧셈만 없다면
        else :
            # 뺄셈 -> 곱셈
            tmpList = numList.copy()
            tmpList = minusRotate(minusIdx, tmpList)
            tmpList = multipleRotate(multipleIdx, tmpList)
            
            # 곱셈 -> 뺄셈
            numList = multipleRotate(multipleIdx, numList)
            numList = minusRotate(minusIdx, numList)
            
            # 절댓값이 큰 값 반환
            if abs(tmpList[0]) < abs(numList[0]) :
                answer = abs(numList[0])
            else :
                answer = abs(tmpList[0])                    
    
    # 뺄셈 역시 덧셈과 같이
    elif len(minusIdx) == 0 :
        if len(plusIdx) == 0 :
            answer = 1
            for m in numList :
                answer *= m
                
        elif len(multipleIdx) == 0 :
            for m in numList :
                answer += m
        else :
            tmpList = numList.copy()
            tmpList = plusRotate(plusIdx, tmpList)
            tmpList = multipleRotate(multipleIdx, tmpList)
            
            numList = multipleRotate(multipleIdx, numList)
            numList = plusRotate(plusIdx, numList)

            if abs(tmpList[0]) < abs(numList[0]) :
                answer = abs(numList[0])
            else :
                answer = abs(tmpList[0])                    
    
    # 나눗셈 역시 위와 같이이
    elif len(multipleIdx) == 0 :
        if len(minusIdx) == 0 :
            for m in numList :
                answer += m
                
        elif len(plusIdx) == 0 :
            answer = numList[0]
            for m in numList[1:] :
                answer -= m
            answer = abs(answer)
        else :
            tmpList = numList.copy()
            tmpList = minusRotate(minusIdx, tmpList)
            tmpList = plusRotate(plusIdx, tmpList)
            
            numList = plusRotate(plusIdx, numList)
            numList = minusRotate(minusIdx, numList)

            if abs(tmpList[0]) < abs(numList[0]) :
                answer = abs(numList[0])
            else :
                answer = abs(tmpList[0])                    

    # 셋 다 존재한다면 6가지 경우의 수 모두 수행
    else :
        tmpList = numList.copy()
        tmpList = minusRotate(minusIdx, tmpList)
        tmpList = plusRotate(plusIdx, tmpList)
        tmpList = multipleRotate(multipleIdx, tmpList)
        answer = abs(tmpList[0])
        
        tmpList = numList.copy()
        tmpList = minusRotate(minusIdx, tmpList)
        tmpList = multipleRotate(multipleIdx, tmpList)
        tmpList = plusRotate(plusIdx, tmpList)
        if answer < abs(tmpList[0]) :
            answer = abs(tmpList[0])
        
        tmpList = numList.copy()
        tmpList = multipleRotate(multipleIdx, tmpList)
        tmpList = minusRotate(minusIdx, tmpList)
        tmpList = plusRotate(plusIdx, tmpList)
        if answer < abs(tmpList[0]) :
            answer = abs(tmpList[0])            
            
        tmpList = numList.copy()
        tmpList = multipleRotate(multipleIdx, tmpList)
        tmpList = plusRotate(plusIdx, tmpList)
        tmpList = minusRotate(minusIdx, tmpList)
        if answer < abs(tmpList[0]) :
            answer = abs(tmpList[0])            
    
        tmpList = numList.copy()
        tmpList = plusRotate(plusIdx, tmpList)
        tmpList = multipleRotate(multipleIdx, tmpList)
        tmpList = minusRotate(minusIdx, tmpList)
        if answer < abs(tmpList[0]) :
            answer = abs(tmpList[0]) 
            
        numList = plusRotate(plusIdx, numList)
        numList = minusRotate(minusIdx, numList)
        numList = multipleRotate(multipleIdx, numList)
        if answer < abs(numList[0]) :
            answer = abs(numList[0]) 
    return answer