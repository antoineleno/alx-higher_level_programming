#!/usr/bin/node

const NumberOfArguments = process.argv.length - 2;
mynumber = [];
if (NumberOfArguments === 0 || NumberOfArguments === 1) {
  console.log(0);
} else {
  for (let i = 2; i < NumberOfArguments + 2; i++) {
    const num = Number(process.argv[i]);
    mynumber.push(num);
  }
  const index = mynumber.indexOf(Math.max(...mynumber));
  if (index !== -1) {
        mynumber.splice(index, 1);
  }
  console.log(Math.max(...mynumber));
}
