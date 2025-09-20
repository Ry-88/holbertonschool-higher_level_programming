#!/usr/bin/node

const lines = [
    'C is fun',
    'Python is cool',
    'JavaScript is amazing'
  ];
  
  let output = '';
  let i = 0;
  
  while (i < lines.length) {
    output += lines[i];
    i++;
    // Only add newline if not the last element
    output += i < lines.length ? '\n' : '';
  }
  
  console.log(output);
  