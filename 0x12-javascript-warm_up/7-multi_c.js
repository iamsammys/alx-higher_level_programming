#!/usr/bin/node

let arg = process.argv[2];
if (arg) {
  while (arg > 0) {
    console.log('C is fun');
    arg--;
  }
} else {
  console.log('Missing number of occurrences');
}
