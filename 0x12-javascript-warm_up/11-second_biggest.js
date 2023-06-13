#!/usr/bin/node

const numLst = process.argv;
if (process.argv.length >= 4) {
  const newLst = numLst.slice(2).sort((a, b) => a - b).reverse();
  console.log(newLst[1]);
} else { console.log(0); }
