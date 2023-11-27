# 두 숫자 사이에 거리 측정
def calculateDistance(n1, n2) :
    # 계산의 편의를 위해 각 숫자 -1 씩
    n1 -= 1
    n2 -= 1
    
    # 맨해튼 거리 측정 (피타고라스보다 빠르다)
    diff1 = abs((n1%3)-(n2%3))
    diff2 = abs((n1//3)-(n2//3))
    return diff1+diff2

def solution(numbers, hand):
    # 1~12까지 키패드로 설정 (*:10, #:12)
    answer = ''
    leftHand = 10
    rightHand = 12
    
    # 모든 숫자를 받는다
    for i in range(len(numbers)) :
        
        # 0은 11
        if numbers[i] == 0 :
            num = 11
            
        # 나머지는 그대로 numbers[i]를 받는다
        else :
            num = numbers[i]
        
        # 1, 4, 7 -> 왼손
        if (num%3) == 1 :
            leftHand = num
            answer += 'L'
            
        # 3, 6, 9 -> 오른손
        elif (num%3) == 0 :
            rightHand = num
            answer += 'R'
            
        # 나머지는 맨해튼 거리 비교
        else :
            leftDiff = calculateDistance(leftHand, num)
            rightDiff = calculateDistance(rightHand, num)
            
            # 오른손이 가까우면 오른손
            if leftDiff > rightDiff :
                rightHand = num
                answer += 'R'
                
            # 왼손이 가까우면 왼손
            elif leftDiff < rightDiff :
                leftHand = num
                answer += 'L'
                
            # 똑같으면 어느 손잡이인지 고려
            else :
                if hand == "right" :
                    rightHand = num
                    answer += 'R'
                else :
                    leftHand = num
                    answer += 'L'
            
    return answer