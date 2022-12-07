#!/usr/bin/node
let count = 0;

module.exports.logMe = function (item) {
  count += 1;
  console.log(`${count}: ${item}`);
};
