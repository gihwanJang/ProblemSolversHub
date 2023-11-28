let expression = "100-200*300-500+20";
console.log(solution(expression));

function solution(expression) {
    var answer = 0;
    let [expressionArray, operators] = stringSplitor(expression);
    answer = calculateMaxValue(expressionArray, operators);
    return answer;
}

function calculateMaxValue(expressionArray, operators) {
    let maxValue = 0;
    let operatorList = priorityOperator(operators);

    for (let operPriority of operatorList) {
        let tmpValue = calculate(expressionArray, operPriority);
        if (maxValue < tmpValue) {
            maxValue = tmpValue;
        }
    }

    function calculate(expressionArray, operPriority) {
        let copyArray = expressionArray.slice();

        for (let oper of operPriority) {
            let tmpArray = [];
            for (let idx = 0; idx < copyArray.length; idx++){
                if (copyArray[idx] === oper) {
                    tmpArray[tmpArray.length - 1] = eval(tmpArray[tmpArray.length - 1] + copyArray[idx] + copyArray[idx+1]);
                    idx++;
                }
                else {
                    tmpArray.push(copyArray[idx]);
                }
            }
            copyArray = tmpArray;
        }
        return Math.abs(copyArray[0]);
    }

    return maxValue;
}


function priorityOperator(operators){
    let operSet = Array.from(new Set(operators));
    let operatorsArray = [];
    permuteOperator(operSet, [], operatorsArray);

    function permuteOperator(operators, currentPermutation, allPermutations) {
        if (currentPermutation.length === operators.length) {
            allPermutations.push(currentPermutation.slice());
            return;
        }
    
        for (var i = 0; i < operators.length; i++) {
            if (!currentPermutation.includes(operators[i])) {
                currentPermutation.push(operators[i]);
                permuteOperator(operators, currentPermutation, allPermutations);
                currentPermutation.pop();
            }
        }
    }

    return operatorsArray;
}

function stringSplitor(expression) {
    let regex = /(\d+|\D)/g;
    let expressionArray = expression.match(regex);
    let operators = [];

    expressionArray.forEach(function (element) {
        if (isNaN(element)) {
            operators.push(element);
        }
    });

    return [expressionArray, operators];
}