let gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]	;
console.log(solution(gems));

function solution(gems) {
    let answer = [];
    answer = twoPointerRange(gems)
    return answer;
}

function twoPointerRange(gems) {
    const totalGemCount = new Set(gems).size;

    let gemCount = new Map();
    let left = 0;
    let right = 0;
    let minRange = [0, gems.length - 1];
    
    while (right < gems.length) {
        if (!gemCount.has(gems[right])) {
            gemCount.set(gems[right], 1);
        } else {
            gemCount.set(gems[right], gemCount.get(gems[right]) + 1);
        }
        
        while (gemCount.size === totalGemCount) {
            if (right - left < minRange[1] - minRange[0]) {
                minRange = [left, right];
            }
            
            gemCount.set(gems[left], gemCount.get(gems[left]) - 1);
            
            if (gemCount.get(gems[left]) === 0) {
                gemCount.delete(gems[left]);
            }
            left++;
        }
        right++;
    }
    return [minRange[0] + 1, minRange[1] + 1];
}