#!/usr/bin/node
let args = process.argv.length;
console.log(`${args === 0 ? 'No a' : 'a'}rgument${args === 1 ? ' found' : (args > 1 ? 's found' : '')}`);
