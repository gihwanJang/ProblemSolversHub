## 풀이

- 이 문제는 수학 문제이다. 
<br>

나는 이렇게 판단하면서 풀었다. 

10^n 일때 n의 숫자만큼 자리수가 증가한다. 
그렇다면 a^n일 때, a를 10처럼 맞춰주면 되지 않을까 생각했다. 

$$\log_b a$$ 
b = 10 이면 즉, 밑이 10이면 a가 10이 되기 위해서 얼마냐 부족하냐로 생각할 수 있고 
즉 그 값이 자리수를 의미한다. 

$$a^b$$

일때, $$ b * \log a== 자리수 $$ 
로 생각할 수 있다. 여기서 값이 소수점이 나오기때문에 +1 해주면 답이 된다. 


