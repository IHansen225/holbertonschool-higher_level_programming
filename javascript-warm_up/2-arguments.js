#!/usr/bin/node
const args = process.argv.length;
console.log(`${args === 0
    ? 'No a'
    : 'A'}rgument${args === 1
        ? ' found'
        : (args > 1
            ? 's found'
            : '')}`);
