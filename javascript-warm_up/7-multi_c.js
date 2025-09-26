#!/usr/bin/node

const arg = process.argv[2];
const x = parseInt(arg, 10);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
