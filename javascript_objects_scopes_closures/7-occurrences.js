#!/usr/bin/node
module.exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const elem of list) {
    count = elem === searchElement ? count + 1 : count;
  }
};
