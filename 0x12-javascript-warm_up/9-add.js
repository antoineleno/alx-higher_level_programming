#!/usr/bin/node

function add (a, b) {
  return a + b;
}
const myarg = process.argv[2];
const secondarg = process.argv[3];
const firstNum = Number(myarg);
const secondnumber = Number(secondarg);

if (!isNaN(firstNum) && !isNaN(secondnumber)) {
  console.log(add(firstNum, secondnumber));
} else {
  console.log('NaN');
}
