# 풀이

### 생각의 흐름
처음에 단순한 수학적 아이디어와 구현이라고 생각했다.<br>
하지만 꼭 오른쪽 아래 방향으로만 내려가는것이 아니라,<br>
돌아서 가는 길이라도 빠른 길이 중요하다는 것을 듣고<br>
백트래킹을 사용하여 완성하였다.

### 백트래킹
동서남북 방향을 모두 고려하여 제일 끝점(N-1, N-1)에서 까지의 거리가<br>
최소인 지점을 현재 위치에 넣어서 그것을 시작점 (0,0)까지 진행

---

### 다른 코드와의 비교 및 느낀점
- Python에서 가장 빠른 코드<br>
=> (0,0) ~ (N-1, N-1) 까지 반복문으로 최소점을 찾기 +<br>
최소점을 찾는 리스트를 1차원으로 구현

- Python에서 가장 적은 메모리를 소요하는 코드<br>
=> 제일 빠른 코드와 같은 방식 (1차원 구현이 핵심)

- Python에서 가장 짧은 코드
=> deque와 비트를 사용하여 구현
```python
from collections import deque
 
dx=[0,0,1,-1];dy=[1,-1,0,0] 
for t in range(int(input())):
    n=int(input())
    m=[[*map(int, list(input()))]for _ in range(n)]
    d=[[1<<32]*n for _ in range(n)]
    d[0][0]=0
    q=deque()
    q.append((0,0))
    while q:
        y,x=q.popleft()
        for i in range(4):
            ny,nx=y+dy[i],x+dx[i]
            if 0<=ny<n and 0<=nx<n:
                if d[ny][nx]>d[y][x]+m[ny][nx]:d[ny][nx]=d[y][x]+m[ny][nx];q.append((ny,nx))
    print(f'#{t+1}',d[n-1][n-1])
```