# (30046) HJS
## :100: Algorithm
[문제 바로가기](https://www.acmicpc.net/problem/30046)
#
## 문제
2123년에는 수를 표현하는 색다른 방식인 "홍진수"가 존재한다.

홍진수는 총 3가지의 문자 H, J, S로 이루어진 문자열로, 각 문자 H, J, S에 $1$ 부터 $9$ 까지의 숫자를 서로 중복되지 않게 하나씩 대입하여 수를 표현할 수 있다. 예를 들어, 홍진수 HJSHJH는 $358353$, $914919$ 는 표현할 수 있지만, $131131$, $555555$ 는 표현할 수 없다.

길이가 같은 세 개의 홍진수 $P$, $Q$, $R$ 이 주어졌을 때, 각 홍진수가 표현하는 수 $p$ , $q$ , $r$ 이 $p$ < $q$ < $r$ 을 만족하게 하는 H, J, S가 존재하는지 확인하자. H, J, S에 대입한 수는 $P$, $Q$, $R$ 이 모두 공유한다.
#
## 입력
첫 번째 줄에는 $P$, $Q$, $R$ 의 길이 $N$ 이 주어진다. 두 번째 줄부터 세 개의 줄에 걸쳐 문자열 $P$, $Q$, $R$ 이 차례대로 주어진다.  $(1 \le N \le )$
## 출력
첫 번째 줄에 조건에 맞는 H, J, S가 존재한다면 HJS! HJS! HJS!를 출력하고, 그렇지 않으면 Hmm...를 출력한다.
