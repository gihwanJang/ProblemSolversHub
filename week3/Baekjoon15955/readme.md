# (15955) 부스터
## :100: Algorithm
[문제 바로가기](https://www.acmicpc.net/problem/15955)
#
## 문제

![img1](https://upload.acmicpc.net/c2bada33-0a9b-4fe1-b28b-c6bb2ca7f25f/-/preview/)

최근 새로 출시되어 인기를 끌고 있는 카카오게임이 있다. 이 게임에서는 2차원 좌표 평면상에 N개의 체크포인트가 존재하며, 플레이어는 체크포인트를 오가면서 원하는 곳에 도달해야 하는 목표를 가진다.

플레이어가 조종하는 캐릭터는 최대 HP 제한 X를 가지며, 또한 부스터를 장착하고 있다. 이 캐릭터는 다음과 같은 두 가지 방법으로 이동할 수 있다.

걷기: 단순한 걷기 동작이다. 원하는 방향으로 걸어갈 수 있다. d만큼의 거리를 걸어갔을 때, 캐릭터의 HP는 d만큼 감소한다. HP가 0 미만이 될 경우 캐릭터는 죽게 된다.
부스터 사용: 플레이어는 동 / 서 / 남 / 북 4가지 방향으로 부스터를 사용할 수 있다. (동: x좌표 증가, 서: x좌표 감소, 남: y좌표 감소, 북: y좌표 증가) 부스터를 활성화하면, 캐릭터는 HP를 소모하지 않고 원하는 방향으로 날아가게 된다. 이후 플레이어가 원하는 위치에서 부스터를 종료하면, 움직임이 멈추고 캐릭터가 그 자리에 서게 된다.
부스터는 "방전"과 "충전"의 두 가지 상태를 가지며, 충전 상태에만 사용될 수 있다. 부스터를 종료하면, 부스터는 이동 거리에 상관없이 방전된다.

초기에, 플레이어의 HP는 X이며, 플레이어의 부스터는 방전되어 있다. 각각의 체크포인트에서 플레이어는 HP를 최대 한번 재충전할 수 있으며 (즉, 최대 HP인 X로 바꿀 수 있으며), 방전된 부스터를 최대 한번 재충전할 수 있다.

동현이는 이 게임의 개발자이며, 현재 게임의 세부 사항을 조정하고 있다. 다양한 스테이지의 개발을 위해서, 동현이는 다음과 같은 질의를 빠르게 처리해야 한다.

플레이어의 최대 HP 제한이 X일 때, 체크포인트 A에서 시작하여서 체크포인트 B로 이동할 수 있는 방법이 있는가?
동현이를 도와, 각각의 질의를 처리하라.
#
## 입력
첫 번째 줄에 체크포인트의 수 N, 질의의 수 Q가 주어진다. (1 ≤ N, Q ≤ 250,000)

이후 N개의 줄에 체크포인트의 좌표를 나타내는 두 정수 Xi, Yi가 주어진다. (Xi, Yi) 위치에 i번 체크포인트가 있음을 뜻한다. 모든 체크포인트의 위치는 서로 다르다. (-109 ≤ Xi, Yi ≤ 109)

이후 Q개의 줄에 각각의 질의를 나타내는 세 정수 Ai, Bi, Xi가 주어진다. Ai번 체크포인트에서 Bi번 체크포인트로 최대 HP 제한 Xi 상태에서 움직일 수 있는지를 묻는 질의이다. (1 ≤ Ai, Bi ≤ N, 0 ≤ Xi ≤ 109)
## 출력
Q개의 줄에 각각의 질의의 결과를 YES 또는 NO로 순서대로 출력한다.