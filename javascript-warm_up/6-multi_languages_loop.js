#!/usr/bin/node

// Array of lines
const lines = [
    'C is fun',
    'Python is cool',
    'JavaScript is amazing'
  ];
  
  // Initialize an empty string
  let output = '';
  
  // Loop through the array and append each line with a newline character
  for (let i = 0; i < lines.length; i++) {
    output += lines[i];
  }
  
  // Print all lines at once
  console.log(output);
