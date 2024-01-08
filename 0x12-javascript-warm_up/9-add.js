#!/usr/bin/node
const [, , a, b] = process.argv;
function add(a, b) {
  return parseInt(a) + parseInt(b);
}
console.log(add(a, b));
