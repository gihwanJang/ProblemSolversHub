import sys
import math
input = sys.stdin.readline

# 입력 받기
N = int(input())
testTakers = list(map(int, input().split()))
B, C = map(int, input().split())

# 총 감독관 수
totalSupervisors = 0

# 시험장 당 응시자 순서대로
for i in testTakers :
    # 총감독관으로 커버된다면 + 1
    if i <= B :
        totalSupervisors += 1
        
    # 부감독관이 필요하다면 인원수 만큼 + 1(총감독관)
    # 이 때 부감독관의 인원수 : (전체인원 - 총감독관 관리인원)/부감독관 관리인원 의 올림
    else :
        i -= B
        totalSupervisors += math.ceil(i/C) + 1

print(totalSupervisors)