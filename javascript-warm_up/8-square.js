#!/usr/bin/node
if (!(isNaN(parseInt(process.argv[2], 10)))) {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log('X'.repeat(parseInt(process.argv[2])));
  }
} else {
  console.log('Missing size');
}
