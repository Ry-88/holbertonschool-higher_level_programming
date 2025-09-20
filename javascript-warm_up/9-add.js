#!/usr/bin/node

// Get the arguments
const a = parseInt(process.argv[2], 10)
const b = parseInt(process.argv[3], 10)

// Define the addition function
function add(x, y) {
  return x + y
}

// Print the result of the addition
console.log(add(a, b))
