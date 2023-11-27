def solution(gems):
    
    # gems 배열을 set으로 바꾸기
    gemSet = set(gems)
    
    # gemSet의 길이 측정
    lenGemSet = len(gemSet)
    
    # gem이 하나밖에 없다면 [1, 1] 출력
    if lenGemSet == 1 :
        return [1, 1]
    
    # gems의 개수와 gemSet의 개수가 같다면 처음부터 끝까지 출력
    elif lenGemSet == len(gems) :
        return [1, lenGemSet]
    
    # gemDict 생성 후 gemSet의 보석을 value 0으로 저장
    gemDict = {}
    for p in gemSet :
        gemDict[p] = 0
    
    # 연속된 보석의 차이 (infinity로 초기화)
    diff = float("inf")
    
    # 연속된 보석 시작
    start = 0
    
    # 연속된 보석 끝
    end = 0
    
    # 가장 절대 위치가 작은 보석 종류
    mnGem = None
    
    # 가장 절대 위치가 작은 보석 개수 (infinity로 초기화)
    mn = float("inf")
    
    # 계산 단순화를 위한 bool
    passing = False

    # gems의 모든 항목 체크
    for i in range(len(gems)) :
        
        # gems의 종류 판별
        gemsType = gems[i]
        
        # 해당되는 gems에 위치(index)값 넣기
        gemDict[gemsType] = i+1

        # 만약 가장 앞에 있는 보석이 바뀌면
        if gemsType == mnGem :
            # 재 측정 후 새 보석으로 교체
            mnGem = min(gemDict, key=gemDict.get)
            mn = gemDict[mnGem]
            
            # 가장 뒤에 값은 항상 갱신된다
            mx = i+1
            
            # 보석의 차이
            tmpDiff = mx - mn
            
            # 기존의 보석보다 차이가 작을 때만 갱신
            # (같더라도 가장 작은 값이 먼저이므로 >)
            if diff > tmpDiff :
                diff = tmpDiff
                start = mn
                end = mx

        # 모든 보석이 dict에 넣어졌을 때 (gemDict.values가 0이없을 때)
        if passing is False and 0 not in gemDict.values() :
            # 가장 앞에 있는 보석 찾기
            mnGem = min(gemDict, key=gemDict.get)
            mn = gemDict[mnGem]
            
            # 가장 뒤에 있는 보석은 항상 i+1
            mx = i+1
            
            # 둘 사이의 차이 비교 후 삽입
            tmpDiff = mx - mn
            if diff > tmpDiff :
                diff = tmpDiff
                start = mn
                end = mx
                
            # 다시는 이 항목을 시행하면 안되므로 True 선언
            passing = True        
    
    return [start, end]