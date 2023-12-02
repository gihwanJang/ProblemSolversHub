# 풀이

- 그래프 탐색, 다익스트라 알고리즘

1. 다익스트라의 distance배열의 정보를 저장하는 Location 클래스
    - row : 좌표의 row값 저장
    - col : 좌표의 column값 저장
    - dis : distance(거리) 값 저장
    - dir : direct(진행 방향)값 저장
    - compareTo(other) : 거리 비교 함수

2. 다익스트라를 진행하는 Solution 클래스 선언
    - board : 입력받은 board배열
    - size : board의 크기
    - distance : 각 좌표의 진행 방향의 cost값을 저장
    - #initDistance : distance배열 초기화
        - (0, 0)은 거리가 0이므로 초기화
    
    - dijkstra() : 알고리즘을 진행하는 함수
    - getCost(next, curr) : 현재 좌표와 다음 좌표를 비교하여 같은 방향으로 진행하는지 확인하고 비용을 return하는 함수
        - 같은 방향 : return 100
        - 다른 방향 : return 600
    - isValidate(r, c) : 범위를 초과하는지 확인하는 함수

3. Solution객체의 dijkstra() 함수
    - 방향을 확인하는 dx, dy 변수
    - 이동 정보를 저장하는 pq 배열 변수
    - (0,0) 에서 시작하는 (1,0), (0,1)에 대해 이동 정보를 pq에 저장
    - 반복문을 통해 pq에 값이 없을 때까지 진행
        - pq.shift()를 통해 curr에 저장
        - curr.dis와 this.distance[curr좌표 및 방향]을 비교하여 가장 짧은 경로를 distance[현재좌표]에 저장
        - 4방향을 확인하여 nextR, nextC에 저장
        - next가 진행 가능하면 Location을 distance에 저장
            - 이때 getCost를 통해 비용을 갱신시킴
        - 반복

4. while문이 끝났을 때 distance[size-1 좌표의 정보] 확인
    - (size-1, size-1)에 도착할 수 있는 경우의 수
        - 왼쪽에서 오른쪽 : distance[size-1][size-1][1]
        - 위에서 아래 : distance[size-1][size-1][3]
        - 두개의 값 중 작은 값이 최소 비용
    - 최소 비용을 return