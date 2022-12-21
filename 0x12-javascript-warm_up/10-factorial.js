#!/usr/bin/node
const arg = +process.argv[2];
function factorial (arg) {
  if ((arg === 0 || isNaN(arg))) {
    return 1;
  } else {
    return factorial(arg - 1) * arg;
  }
}
const fact = factorial(arg);
console.log(fact);
