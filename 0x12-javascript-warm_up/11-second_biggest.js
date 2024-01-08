#!/usr/bin/node
const [, , ...args] = process.argv;
if (args.length < 2) {
  console.log(0);
}
const sorted = args.sort((a, b) => a - b);
console.log(sorted[sorted.length - 2]);
