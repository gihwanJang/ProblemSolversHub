const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');

let typing = input[0];
let type = ['fdsajkl;', 'jkl;fdsa', 'asdf;lkj', ';lkjasdf', 'asdfjkl;', ';lkjfdsa'];
let typeName = ['in-out', 'out-in', 'stairs', 'reverse', 'molu'];

switch(typing){
    case type[0] : 
    case type[1] : console.log(typeName[0]); break;
    case type[2] : 
    case type[3] : console.log(typeName[1]); break;
    case type[4] : console.log(typeName[2]); break;
    case type[5] : console.log(typeName[3]); break;
    default : console.log(typeName[4]); break;
}