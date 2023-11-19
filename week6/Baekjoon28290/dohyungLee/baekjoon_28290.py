def main() :
    strInput = input()
    classifyInput(strInput)

# 입력에 따라 정렬해주는 함수
def classifyInput(strInput) :
    
    # 받은 입력에 따라 분류하여 출력
    if strInput == "fdsajkl;" or strInput == "jkl;fdsa" :
        print("in-out")
    elif strInput == "asdf;lkj" or strInput == ";lkjasdf" :
        print("out-in")
    elif strInput == "asdfjkl;" :
        print("stairs")
    elif strInput == ";lkjfdsa" :
        print("reverse")
    else :
        print("molu")

if __name__ == "__main__" :
    main()