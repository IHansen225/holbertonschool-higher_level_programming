#!/usr/bin/node
if (!(isNaN(parseInt(process.argv[1], 10)))) {
  for (let i = 0; i < parseInt(process.argv[1], 10); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
