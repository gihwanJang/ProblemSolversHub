# 풀이

해당 문제는 제곱수 즉 (4, 9, 16 ...)과 같은 수로 나누어 떨어지지 않는 수 중 k번째의 수를 찾는 것이 목표입니다.  
즉 주어진 수를 소인수 분해를 했을 시 같은 수가 2개 이상 나오면 안됩니다.  
그러므로 해당 수는 각 소인수들의 곱들로 조합된 수의 제곱을 제외한 모든 수입니다.  

우선 에라토스테네스의 체를 이용하여 소수를 먼저 구해줍니다.  
해당 소수들의 이용하여 조합을 만들고 해당 조합의 제곱을 주어진 수에 나누면 해당 주어진 수 까지 해당 조합의 제곱수에 대하여 모두 구할 수 있습니다.  

이때 위의 조합을 모두 구하여 넣게 된다면 해당 수의 중복이 발생합니다.  
예를 들어 100은 4 또는 25로 나누어 떨어집니다.  
그러므로 2, 5를 선택한 경우는 개수를 차등해줍니다.  
위와 같은 규칙을 따르면 소수 홀수 개로 조합하는 경우 합산 짝수 개로 조합하는 경우 감산해줍니다.  

위의 과정을 통하여 제곱수를 빼면 특정 값에 대한 제곱 수를 찾을 수 있고 특정 값에서 제곱수를 빼주면 해당 값까지의 제곱ㄴㄴ수를 찾을 수 있습니다.  

하지만 1~2e9값들 중 특정 값을 찾아야 합니다.  
이것을 선형에 하게되면 너무 많은 과정을 거치기 때문에 제곱ㄴㄴ수는 특정 값에 대하여 오름차순이기 때문에 해당 특정 값을 이진 탐색을 통해 찾아줍니다.