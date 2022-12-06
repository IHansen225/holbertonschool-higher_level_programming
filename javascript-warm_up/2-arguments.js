#!/usr/bin/node
const args = process.argv.length;
console.log(`${args === 1
    ? 'No a'
    : 'A'}rgument${args === 2
        ? ' found'
        : (args > 2
            ? 's found'
            : '')}`);
