#!/usr/bin/node
if (process.argv.length === 1 || process.argv.length === 2) {
  console.log(0);
} else {
  const nums = [];
  for (let i = 1; i < process.argv.length; i++) { nums.push(process.argv[i]); }
  nums.sort(function (a, b) { return a - b; });
  console.log(nums[nums.length - 2]);
}
