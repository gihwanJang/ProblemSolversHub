## 풀이 

사다리 타기 문제 
사다리는 밑으로 내려가고 왼쪽 오른쪽 길목을 만나면 무조건 들어간다. 도착지가 나올 때까지 반복한다. 
이를 구현하는 문제이다.

어차피 x 좌표는 주어지기 때문에 위가 아닌 밑에서 부터 진행했다.

도착지 좌표를 넣고 dfs를 시작한다. 
visited를 체크하면서 왼쪽, 오른쪽, 위 순서로 갈 수 있으면 간다. 



위 조건대로 갈 수 없다 == 도착했다.(사다리 입력 조건이 도착지로 못가는 경우가 없기 때문에)

결과를 출력하면 된다.


