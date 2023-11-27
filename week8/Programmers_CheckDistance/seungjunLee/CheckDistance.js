places = [["POOPO", "OOOOO", "OOOXP", "POOPX", "OOOOO"], 
        ["POOPO", "OOOOO", "OOOXP", "OPXPX", "OOPOO"], 
        ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
        ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

console.log(solution(places));

function solution(places) {
    var answer = [];
    for (let waitingRoom of places) {
        answer.push(checkDistance(waitingRoom));
    }

    return answer;
}

function checkDistance(waitingRoom) {
    waitingRoom = waitingRoom.map(function (element) {
        return [... element];
    });

    for (let i = 0; i < 5; i++) {
        for (let j = 0; j < 5; j++) {
            if (waitingRoom[i][j] == 'P'){
                if(BFS(i,j,waitingRoom)){
                    return 0;
                }
            }
        }
    }
    
    return 1;
}

function BFS(y, x, waitingRoom) {
    const visited = Array.from(Array(5), () => Array(5).fill(false));
    visited[y][x] = true;
    let moveQue = rangeCheck(y, x);
    let moveDistance = 1;

    function rangeCheck(i, j) {
        const moveX = [1, 0, -1, 0];
        const moveY = [0, 1, 0, -1];

        let que = [];
        for (let move = 0; move < 4; move++) {
            const newX = j + moveX[move];
            const newY = i + moveY[move];
            if (newY >= 0 && newY < 5 && newX >= 0 && newX < 5 && waitingRoom[newY][newX] !== 'X' && !visited[newY][newX]) {
                que.push([newY, newX]);
                if (waitingRoom[newY][newX] !== 'P') {
                    visited[newY][newX] = true;
                }
            }
        }
        return que;
    }

    while (moveDistance <= 2 && moveQue.length > 0) {
        const currPos = moveQue.slice();
        moveQue = [];
        for (const element of currPos) {
            if (waitingRoom[element[0]][element[1]] === 'P' && !visited[element[0]][element[1]]) {
                return true;
            }
            moveQue.push(...rangeCheck(element[0], element[1]));
        }
        moveDistance++;
    }
    return false;
}
