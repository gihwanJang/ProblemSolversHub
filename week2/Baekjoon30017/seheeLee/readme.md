## 풀이

문제 조건에서 패티의 수는 치즈 수 + 1 한 값과 같기 때문에, 만들 수 있는 버거의 수는 패티 + (패티 - 1 ) 수와 같다. 

여기서 예외 조건이 있다. 만약 치즈 수가 패티-1 보다 적은 경우(ex 패티:4장 치즈 2장)일 때에는 패티의 수가 충만하니까 치즈 + (치즈+1) 한 값으로 계산하면 된다. 
