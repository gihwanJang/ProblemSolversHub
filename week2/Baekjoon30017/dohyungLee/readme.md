# 풀이

### 생각의 흐름
해당 문제를 풀기 위해 저의 생각의 흐름은 다음과 같이 진행되었습니다.

1. main 함수에서 Patty의 개수와 Cheese의 개수를 입력받는다.
2. make_burger 함수에서 치즈버거(burger)의 크기(burger_size)를 반환한다.
3. 반환받은 burger의 크기를 출력한다.

### 치즈버거의 크기
이 때 치즈버거의 크기를 구하기 위해 치즈버거의 특징을 다음과 같이 정의하였습니다.

1. cheese위아래로 patty가 존재해야한다.
2. cheese의 개수가 patty의 개수보다 1개 적을 때 모든 재료가 쓰인다.
3. cheese의 개수가 patty보다 같거나 많다면 cheese는 버려진다.
-> patty를 기준으로 치즈버거의 크기를 계산되어야한다.
4. patty의 개수가 cheese보다 (2개이상) 적다면 patty는 버려진다.
-> cheese를 기준으로 치즈버거의 크기가 계산되어야한다.

이 때 2번 조건은 4번 조건에 포함이 되므로, if 조건문을 통해 3번과 4번 상황으로 나누었습니다.

3번 상황에서 patty + cheese는 patty + (patty - 1) 를 반환합니다.
4번 상황에서 patty + cheese는 (cheese + 1) + cheese 를 반환합니다.

---

# 느낀점 및 수정해야될 사항

- 코드를 조금 더 간소화 할 수 있었습니다.
- 위와 같이 간단한 문제일 떄는 python보다 속도가 빠른 C++, Java를 사용해도 좋을 것 같습니다.