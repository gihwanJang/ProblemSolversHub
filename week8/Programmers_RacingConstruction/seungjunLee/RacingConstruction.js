class Location {
    row;
    col;
    dis;
    dir;

    constructor(r, c, dis, dir) {
        this.row = r;
        this.col = c;
        this.dis = dis;
        this.dir = dir;
    }

    compareTo(other) {
        return this.dis - other.dis;
    }
}

class Solution {
    board;
    size;
    distance;

    constructor(board){
        this.board = board
        this.size = board.length;
        this.distance = this.#initDistance();
    }

    #initDistance(){
        let arr = Array.from({ length: this.size }, () =>
            Array.from({ length: this.size }, () =>
                Array.from({ length: 4 }).fill(Infinity)
        ));

        for (let i = 0; i < 4; i++) {
            arr[0][0][i] = 0;
        }

        return arr;
    }

    dijkstra() {
        let dx = [-1, 1, 0, 0];
        let dy = [0, 0, -1, 1];
        let pq = [];

        if (this.board[0][1] !== 1) {
            pq.push(new Location(0, 1, 100, 3));
        }
        if (this.board[1][0] !== 1) {
            pq.push(new Location(1, 0, 100, 1));
        }

        while (pq.length > 0) {
            const curr = pq.shift();

            if (curr.dis < this.distance[curr.row][curr.col][curr.dir]) {
                this.distance[curr.row][curr.col][curr.dir] = curr.dis;

                for (let i = 0; i < 4; ++i) {
                    const nextR = curr.row + dx[i];
                    const nextC = curr.col + dy[i];

                    if (this.isValidate(nextR, nextC) && this.board[nextR][nextC] !== 1) {
                        pq.push(new Location(nextR, nextC, curr.dis + this.getCost(curr.dir, i), i));
                    }
                }
            }
        }
        return Math.min(this.distance[this.size-1][this.size-1][1], this.distance[this.size-1][this.size-1][3]);
    }

    getCost(next, curr) {
        if ((next < 2 && curr < 2) || (next > 1 && curr > 1)) {
            return 100;
        }
        return 600;
    }

    isValidate(r,c) {
        return (r >= 0 && r < this.size && c < this.size && c >= 0);
    }
}


function solution(board) {
    var answer = 0;
    let solve = new Solution(board);
    answer = solve.dijkstra();
    return answer;
}

let board = [[0,0,1,0],
             [0,0,0,0],
             [0,1,0,1],
             [1,0,0,0]];

console.log(solution(board));