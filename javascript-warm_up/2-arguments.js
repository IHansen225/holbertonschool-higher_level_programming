#!/usr/bin/node
let args = process.argv.length;
console.log(`${args === 1 ? 'No a' : 'a'}rgument${args === 2 ? ' found' : (args > 2 ? 's found' : '')}`);
