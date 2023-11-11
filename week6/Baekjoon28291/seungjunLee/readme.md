# 풀이

- 그래프 탐색

1. 맵의 크기, 레드스톤 갯수, 레드스톤 위치를 입력받은
    - mapSize, redstoneNum, redStonePos

2. 레드 스톤 위치를 입력받을 때, 레드스톤 블록과, 레드스톤 램프, 맵의 모양을 같이 입력받음.
    - redBlockPos, redLampPos, mapShape

3. visited 배열을 false로 초기화함.
4. 직접 구현한 큐 자료구조를 이용하여 BFS를 진행함.
    - redBlockPos 전체를 큐에 넣고 BFS시작

5. 큐에 값이 없거나, 전기신호가 0이 될 때 까지 반복

6. BFS가 종료되었을 때, visited와 redLampPos를 이용하여 redLampPos의 좌표들 전체가 visited true이면 success를 출력하고 램프 좌표 중 하나라도 false 이면 failed를 출력.