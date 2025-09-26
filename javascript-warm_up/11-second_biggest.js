#!/usr/bin/node

// Get the arguments and convert them to integers
const args = process.argv.slice(2).map(a => parseInt(a, 10));

// If less than 2 arguments, print 0
if (args.length < 2) {
  console.log(0);
} else {
  // Sort numbers in descending order
  const sorted = args.sort((a, b) => b - a);
  // Find the second biggest
  console.log(sorted[1]);
}
