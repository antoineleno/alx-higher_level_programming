#!/usr/bin/node

function factorial (a) {
  if (a === 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

if (process.argv[2]) {
  const myarg = process.argv[2];
  const num = Number(myarg);
  console.log(factorial(num));
} else {
  console.log(1);
}
