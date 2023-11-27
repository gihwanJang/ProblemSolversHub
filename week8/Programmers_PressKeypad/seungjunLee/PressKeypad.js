let numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5];
let hand = 'right';
console.log(solution(numbers, hand));

function solution(numbers, hand) {
    var answer = '';
    const leftKeys = [1,4,7];
    const rightKeys = [3,6,9];
    let currentLeft = ['*'];
    let currentRight = ['#'];

    const keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, "#"]];

    for (let button of numbers) {
        if (leftKeys.includes(button)) {
            answer += 'L';
            currentLeft[0] = button;
        }
        else if (rightKeys.includes(button)) {
            answer += 'R';
            currentRight[0] = button;
        }
        else {
            answer += distanceCheck(currentLeft, currentRight,keypad, button, hand);
        }

    }

    return answer;
}

function distanceCheck(left, right, keyPad, button, hand) {
    let leftPos = 0;
    let rightPos = 0;
    let buttonPos = 0;
    let midButton = [2,5,8,0];

    for (let i = 0; i < 4; i++) {
        if (keyPad[i].includes(left[0])) {
            leftPos = i;
        }
        if (keyPad[i].includes(right[0])) {
            rightPos = i;
        }
        if (keyPad[i].includes(button)) {
            buttonPos = i;
        }
    }

    leftPos = Math.abs(leftPos - buttonPos);
    rightPos = Math.abs(rightPos - buttonPos);

    if (!midButton.includes(left[0])) {
        leftPos += 1;
    }
    if (!midButton.includes(right[0])) {
        rightPos += 1;
    }

    if (leftPos === rightPos) {
        let addText = (hand === 'right') ? 'R' : 'L';
        (hand === 'right') ? right[0] = button : left[0] = button;
        return addText;
    }
    if (leftPos > rightPos) {
        right[0] = button;
        return 'R';
    }
    if (leftPos < rightPos) {
        left[0] = button;
        return 'L';
    }
}