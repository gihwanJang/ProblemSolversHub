# 풀이

### 생각의 흐름
1차적으로 숫자를 정렬시킨 후 <br>
가장 최적의 방법으로 그 다음 동작을 실행하게 계획하였습니다.<br>

### 정렬 후 교환교환
교환 시 같은 숫자가 있다면 교환된 숫자 사이에 배치를 바꿀 수 있습니다.<br>
또한 같은 숫자가 존재한다면 두 숫자만 바꿔면 횟수 차감이 됩니다.<br>
위 조건 모두 해당하지 않으면 일의자리-십의자리 교환이 가장 좋습니다.<br>

---

### 다른 코드와의 비교 및 느낀점
- Python에서 가장 빠른 코드<br>
=> 동일 숫자 존재일 때 바로 끝내서 효율성을 극대화했다.<br>

- Python에서 가장 적은 메모리를 소요하는 코드<br>
=> 내꺼다 ㅎㅎ<br>

- Python에서 가장 짧은 코드
=> rough하게 풀었어도 해결은 된다.
```python
for test_case in range(1,int(input())+1):
    num,k=map(str,input().split())
    k=int(k)
    data=set([num])
    sub=set()
 
    for _ in range(k):
        while data:
            s=data.pop()
            s=list(s)
 
            for i in range(len(s)):
                for j in range(i+1,len(s)):
                    s[i],s[j]=s[j],s[i]
                    sub.add("".join(s))
                    s[i],s[j]=s[j],s[i]
        data,sub=sub,data
    print(f"#{test_case} {max(map(int,data))}")
```