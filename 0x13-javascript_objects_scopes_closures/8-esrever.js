#!/usr/bin/node
exports.esrever = function (list) {
  const newLst = [];
  let idx = list.length - 1;
  for (let i = 0; i < list.length; i++) {
    newLst[i] = list[idx];
    idx--;
  }
  return (newLst);
};
