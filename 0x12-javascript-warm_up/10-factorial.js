#!/usr/bin/node
const [, , arg] = process.argv;
function factorial (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  }
  return n * factorial(n - 1);
}
console.log(factorial(parseInt(arg)));
