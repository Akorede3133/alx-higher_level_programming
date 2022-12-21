#!/usr/bin/node
const arg = process.argv[2];
let printValue = '';
if (isNaN(arg)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < arg) {
    let j = 0;
    while (j < arg) {
      printValue += 'X';
      j++;
    }
    console.log(printValue);
    i++;
    printValue = '';
  }
}
