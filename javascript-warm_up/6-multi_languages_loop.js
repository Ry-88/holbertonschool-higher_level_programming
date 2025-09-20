#!/usr/bin/node

// Array of lines
const lines = [
    'C is fun',
    'Python is cool',
    'JavaScript is amazing'
  ];
  
  // Initialize an empty string
  let output = '';
  
  // Loop through the array
  for (let i = 0; i < lines.length; i++) {
    output += lines[i];
    if (i < lines.length - 1) {
      output += '\n';
    }
  }
  
  // Print all lines at once
  console.log(output);
  