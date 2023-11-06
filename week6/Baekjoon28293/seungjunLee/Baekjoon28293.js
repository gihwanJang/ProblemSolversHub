const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
let AB = input[0].split(' ').map(x => +x);
console.log(Math.floor(AB[1] * Math.log10(AB[0]))+1);