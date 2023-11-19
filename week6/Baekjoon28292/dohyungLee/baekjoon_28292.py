def main() :
    # 숫자 입력 받음
    N = int(input())
    
    # 개미수열 중 가장 큰 수를 반환
    antNumRules(N)
    
# 개미 수열을 파악하는 함수
def antNumRules(N) :
    
    # 1, 11
    if N <= 2 : print(1)
    
    # 12, 1121, 122111
    elif N <= 5 : print(2)
    
    # 122213, ... (개미수열은 4가 나올 수 없다)
    else : print(3)
                        
if __name__ == "__main__" :
    main()