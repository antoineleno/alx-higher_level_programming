#!/usr/bin/node

const myarg = process.argv[2];
const num = Number(myarg);

if (!isNaN(num)) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}
