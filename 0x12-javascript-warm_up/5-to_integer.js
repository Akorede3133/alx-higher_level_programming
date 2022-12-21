#!/usr/bin/node
const arg = process.argv[2];
if (isNaN(arg)) {
  console.log('Not a Number');
} else {
  const floated = parseInt(arg);
  console.log(`My number: ${floated}`);
}
