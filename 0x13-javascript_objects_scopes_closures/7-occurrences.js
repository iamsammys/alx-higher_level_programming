#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach(checkItem = item => {
    if (searchElement === item) {
      count += 1;
    }
  });
  return (count);
}
