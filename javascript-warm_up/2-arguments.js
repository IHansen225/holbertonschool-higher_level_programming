#!/usr/bin/node
console.log(`${process.argv.length === 1 ? 'No a' : 'A'}rgument\
${process.argv.length >= 3 ? 's found' : ' found'}`);
