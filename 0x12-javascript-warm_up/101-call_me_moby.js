#!/usr/bin/node

exports.callMeMoby = (x, functions) => {
  while (x) {
    functions();
    x--;
  }
};
