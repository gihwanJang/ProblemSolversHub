# 풀이

### 생각의 흐름
덤프가 가장 높은 부분에서 가장 낮은 부분까지 옮기는 문제입니다.<br>
가장 단순하지만 생각을 많이 안해도되는 구현으로 문제를 풀었습니다.<br>

### 구현
가장 높은 값을 max로 찾습니다.<br>
가장 낮은 값을 min으로 찾습니다.<br>
둘의 차가 1이하가 될때까지 반복해줍니다.<br>
덤프를 모두 수행해도 1보다 크면 그건 그대로 출력해줍니다.<br>

---

### 다른 코드와의 비교 및 느낀점
- Python에서 가장 빠른 코드<br>
=> 높이를 입력받자마자 정렬<br>
=> 높이차 변경 후 정렬 무한반복<br>
[최대, 최소따로 찾는 것보다 정렬이 시간이 빠르다]<br>

- Python에서 가장 적은 메모리를 소요하는 코드<br>
=> 입력 받자마자 정렬시킨 후 위에 방법 반복<br>

- Python에서 가장 짧은 코드
```python
for t in range(10):
 d=int(input());bx=sorted(map(int,input().split()))
 for _ in range(d):bx[0]+=1;bx[-1]-=1;bx.sort()
 print(f'#{t+1} {bx[-1]-bx[0]}')
```