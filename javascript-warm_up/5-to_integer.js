#!/usr/bin/node
console.log(`${
  (isNaN(parseInt(process.argv[1])))
  ? 'Not a number'
  : `My number ${parseInt(process.argv[1])}`
}`);
