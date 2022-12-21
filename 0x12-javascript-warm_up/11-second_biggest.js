#!/usr/bin/node
const args = process.argv;
const array = process.argv.slice(2);
function secondBig (arr) {
  if (args.length === 2 || args.length === 3) {
    return 0;
  }
  let maxNum = Math.max(...arr);
  arr = arr.filter(item => {
    return +item !== maxNum;
  });
  maxNum = Math.max(...arr);
  return maxNum;
}
const result = secondBig(array);
console.log(result);
