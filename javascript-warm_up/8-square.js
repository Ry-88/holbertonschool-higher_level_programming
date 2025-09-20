#!/usr/bin/node

const arg = process.argv[2];
const size = parseInt(arg, 10);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < size) {
    let line = '';
    let j = 0;
    while (j < size) {
      line += 'X';
      j++;
    }
    console.log(line);
    i++;
  }
}
