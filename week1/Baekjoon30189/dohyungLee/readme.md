# 풀이

### 생각의 흐름
해당 문제를 풀기 위해 저의 생각의 흐름은 다음과 같이 진행되었습니다.

1. main 함수에서 문제에 x, y에 해당되는 n과 m을 입력받는다.
2. f(n,m,n+m)로 문제에 해당하는 값을 반환받아 출력한다.

### f(a,b,c)
f(a,b,c)는 문제에 따라
f(a,b,0) + f(a,b,1) + ... + f(a,b,c)를 구해야합니다.

이를 단순히 수학적 계산에 따라 a와 b를 for문으로 이중 중첩 반복하고<br>
해당 값(c)가 나올 때 1을 더해주도록 만들었습니다.<br>
또한 시간을 줄이기 위해 위의 과정을 재귀 함수로 구현했습니다.<br>
단순한 계산이지만 시간을 줄이기 위해 프로그래밍의 기본인 재귀함수를 활용하였습니다.<br>

---

# 느낀점 및 수정해야될 사항

- 삼중 반복으로도 설계가 가능하므로, 걸리는 시간의 비교가 필요합니다.