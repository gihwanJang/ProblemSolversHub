const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
let mapSize = input[0].split(' ').map(x => +x);
let redstoneNum = +input[1];
let redstonePos = [];
let redBlockPos = [];
let redLampPos = [];
let mapShape = Array.from(Array(mapSize[0]), () => new Array(mapSize[1]).fill('nothing'));

for (let i = 0; i < redstoneNum; i++){
    redstonePos.push(input[i+2].split(' '));
    if (redstonePos[i][0] === 'redstone_dust'){
        mapShape[+redstonePos[i][1]][+redstonePos[i][2]] = 'dust';
    }
    if (redstonePos[i][0] === 'redstone_lamp'){
        redLampPos.push([+redstonePos[i][1], +redstonePos[i][2]])
        mapShape[+redstonePos[i][1]][+redstonePos[i][2]] = 'lamp';
    }
    if (redstonePos[i][0] === 'redstone_block'){
        redBlockPos.push([+redstonePos[i][1], +redstonePos[i][2]])
        mapShape[+redstonePos[i][1]][+redstonePos[i][2]] = 'block';

    }
}

class Queue{
    que
    electricity

    constructor(){
        this.que = [];
        this.electricity = 17;
    }

    Push(element) {
        this.que.push(element);
        this.electricity--;
    }

    PopLeft() {
        return this.que.shift();
    }

    isEmpty() {
        if (this.que.length === 0){
            return true;
        }
        return false;
    }
}

function solution(mapSize, mapShape, redBlockPos, redLampPos) {
    let visited = Array.from(Array(mapSize[0]), () => new Array(mapSize[1]).fill(false));

    BFS(visited, mapShape, mapSize, redBlockPos);
    
    return checkLamp(redLampPos, visited);
}

function BFS(visited, mapShape, mapSize, redBlockPos){
    let que = new Queue();
    que.Push(redBlockPos);

    while(!que.isEmpty() && que.electricity > 0) {
        let current = que.PopLeft();
        let tmp = [];

        for (let element of current){
            visited[element[0]][element[1]] = true;
            checkAround(tmp, element, mapShape, mapSize, visited);
        }

        if (tmp.length !== 0){
            que.Push(tmp);
        }
    }
}

function checkAround(tmp, pos, mapShape, mapSize, visited){
    let checkX = [0, 1, 0, -1];
    let checkY = [1, 0, -1, 0];

    if (mapShape[pos[0]][pos[1]] === 'lamp'){
        return;
    }

    for (let i = 0; i < 4; i++){
        if (pos[0] + checkY[i] < 0 || pos[0] + checkY[i] >= mapSize[0]){
            continue;
        }
        if (pos[1] + checkX[i] < 0 || pos[1] + checkX[i] >= mapSize[1]){
            continue;
        }
        if (mapShape[pos[0] + checkY[i]][pos[1] + checkX[i]] !== 'nothing' && visited[pos[0] + checkY[i]][pos[1] + checkX[i]] == false){
            tmp.push([pos[0] + checkY[i], pos[1] + checkX[i]])
        }
    }
}

function checkLamp(redLampPos, visited){
    for (let element of redLampPos){
        if (visited[element[0]][element[1]] === false) {
            return 'failed';
        }
    }
    return 'success';
}

console.log(solution(mapSize, mapShape, redBlockPos, redLampPos));