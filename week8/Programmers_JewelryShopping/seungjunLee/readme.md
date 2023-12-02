# 풀이

- 자료구조(set, map), 투포인터

1. 입력받은 gems 배열을 set으로 형 변환하여 totalGemCount를 계산함.
2. gemCount를 Map 자료형으로 선언하여 투포인터에 따라 들어오고 나가는 보석의 정보를 저장.
    - (ex) ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"] 일 경우
    - left = 0, right = 3 이면 gemCount = {"DIA" : 2, "RUBY" : 2}
3. left = 0, right = 0, minRange = [0, gems.length - 1]로 초기화.
4. while문을 통해 투포인터 진행.
    1. totalGemCount와 gemCount의 크기가 동일하지 않을 경우.
        - gems[right]를 확인.
        - gemCount에 key가 존재하면 key의 value++
        - gemCount에 key가 존재하지 않으면 {"보석 이름" : 1}을 추가
        - right += 1 하고 다시 반복.
    2. totalGemCount와 gemCount가 동일할 경우.
        - minRange범위보다 현재 [left,right]범위가 더 작을 경우 minRange에 저장.
        - gems[left]를 확인하여 gemCount에서 gem[left]의 key를 찾아서 value(카운트) -= 1.
        - 만약 gemCount의 value가 0이 되면 gemCount에서 key값 삭제.
        - left += 1 하고 다시 반복.
5. minRange 범위 return.