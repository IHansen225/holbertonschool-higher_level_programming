#!/usr/bin/node
if (!(isNaN(parseInt(process.argv[1], 10)))) {
  for (let i = 0; i < parseInt(process.argv[1]); i++) {
    console.log('x'.repeat(parseInt(process.argv[1])));
  }
} else {
  console.log('Missing size');
}
