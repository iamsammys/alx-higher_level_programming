#!/usr/bin/node

const factorial = number => {
  if (number > 0) { return (factorial(number - 1) * number); } else { return (1); }
};
const num = parseInt(process.argv[2]);
if (num) { console.log(factorial(num)); } else { console.log(1); }
