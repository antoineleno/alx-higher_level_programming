#!/usr/bin/node

if (process.argv[2]) {
  const myarg = process.argv[2];
  const num = Number(myarg);
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
