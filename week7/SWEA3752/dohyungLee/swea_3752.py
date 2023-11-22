T = int(input())
 
for test_case in range(1, T + 1):
     
    N = int(input())
    testScoreList = list(map(int, input().split()))
    mxNum = max(testScoreList)
     
    scoreCalculateList = [[] for _ in range(mxNum)]
    scoreSet = set()
     
    for i in testScoreList :
        if i != 0 :
            scoreCalculateList[i-1].append((len(scoreCalculateList[i-1])+1)*i)
    for i in range(mxNum) :
        tmpSet = set()
        for a in scoreCalculateList[i] :
            for b in scoreSet :
                tmpSet.add(a+b)
        scoreSet.update(scoreCalculateList[i])
        scoreSet |= tmpSet        
     
    print(f"#{test_case} {len(scoreSet)+1}")