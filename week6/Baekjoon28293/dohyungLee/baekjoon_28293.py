import sys
input = sys.stdin.readline
import math

# 정수 a,b를 공백으로 입력 받음
a, b = map(int, input().split())

# 자릿수를 출력하기 위해 log 사용
result = b*math.log10(a)

# 자릿수 출력 (a=1일 때는 1)
if result == 0 :
    print(1)
else :
    print(int(result) + 1)