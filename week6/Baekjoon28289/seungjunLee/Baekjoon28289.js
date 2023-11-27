const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
let P = +input[0];
let pList = [];
for (let i = 1; i <= P; i++){
    pList.push(input[i].split(' ').map(x => +x));
}
let classCount = [0,0,0,0];

for (let element of pList){
    if(element[0] === 1){
        classCount[3]++;
    }
    else{
        let tmp = element[1];
        switch(tmp){
            case 1 :
            case 2 : classCount[0]++; break;
            case 3 : classCount[1]++; break;
            case 4 : classCount[2]++; break;
        }
    }
}

for (let i = 0; i < 4; i++){
    console.log(classCount[i]);
}