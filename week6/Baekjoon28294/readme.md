# (28294) 프랙탈
## :100: Algorithm
[문제 바로가기](https://www.acmicpc.net/problem/28294)
#
## 문제
프랙탈은 자기 자신을 반복적으로 포함하는 도형을 뜻한다. 대표적으로 시에르핀스키 삼각형, 드래곤 커브가 있다.

ska1xo2dnd3는 프랙탈을 아주 좋아해서 자신만의 프랙탈 패턴을 만들었다. ska1xo2dnd3이 만든 프랙탈 패턴은 다음과 같다.

1. 한 변이 
$N^a$의 길이를 가지는 정
$N$각형에서 시작한다.
2. 각 변의 중앙에서 한 변의 길이를 그 변의 
$\frac{1}{N}$의 길이로 가지는 정
$N$각형을 만든다.

3. 새로 만들어진 정
$N$각형에도 2를 반복한다.

다음 그림은 각각 정4각형과 정5각형에서의 경우를 나타낸 예시다.

![img1](https://upload.acmicpc.net/ce294002-7554-4900-8ae3-00d0b96d363a/-/preview/)
![img2](https://upload.acmicpc.net/dafedb5f-7755-47d7-a8db-47b12cbf2dff/-/preview/)


midori는 이 프랙탈의 둘레를 구하고 싶다. 그러나 midori는 유리수를 싫어하기 때문에 프랙탈 패턴을 그리다가, 새로 만들어진 도형의 변의 길이가 1이 될 때까지만 패턴을 만든 후 도형의 둘레를 계산하기로 했다.

midori의 계산을 도와줄 프로그램을 작성하자. 단, 결괏값이 너무 커질 수 있으니 
$1\,000\,000\,007(10^9+7)$으로 나눈 나머지를 출력한다.
#
## 입력
첫째 줄에 정수 
$N$, 
$a$가 공백으로 구분되어 주어진다. 
$(3 \le N \le 10^9; 1 \le a \le 10^9)$ 
#
## 출력
문제의 정답을 출력한다.