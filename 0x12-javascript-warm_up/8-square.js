#!/usr/bin/node
const arg = process.argv[2];
if (isNaN(arg)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < arg) {
    let j = 0;
    let printValue = '';
    while (j < arg) {
      printValue += 'X';
      j++;
    }
    console.log(printValue);
    i++;
  }
}
