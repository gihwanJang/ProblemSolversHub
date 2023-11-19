def main() :
    P = int(input())
    studentInfo = list()
    
    # 학생 정보 입력
    for _ in range(P) :
        studentInfo.append(list(map(int, input().split())))
        
    # 분류된 과에 따라 출력
    p1, p2, p3, p4 = classify(studentInfo)
    print(p1)
    print(p2)
    print(p3)
    print(p4)
        
# 학생을 분류하는 함수
def classify(studentInfo) :
    firstGrade = 0
    softwareClass = 0
    embeddedClass = 0
    aiswClass = 0
    
    # 학년에 따라 분류
    for i in studentInfo :
        if i[0] == 1 :
            firstGrade += 1
        else :
            if i[1] == 4 :
                aiswClass += 1
            elif i[1] == 3 :
                embeddedClass += 1
            else :
                softwareClass += 1
    
    return softwareClass, embeddedClass, aiswClass, firstGrade
    
if __name__ == "__main__" :
    main()