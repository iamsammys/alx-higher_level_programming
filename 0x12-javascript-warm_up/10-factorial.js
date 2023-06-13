#!/usr/bin/node

const num = parseInt(process.argv[2]);
const factorial = number => {
  if (number > 0) {
    return (factorial(number - 1) * number);
  } else {
    return (1);
  }
};
if (num) {
  const res = factorial(num);
  console.log(res);
} else {
  console.log(1);
}
