#!/usr/bin/node
const args = process.argv.length;
console.log(`${args === 1
  ? 'No argument'
  : (args === 2
    ? 'Argument found'
    : 'Arguments found')}`);
