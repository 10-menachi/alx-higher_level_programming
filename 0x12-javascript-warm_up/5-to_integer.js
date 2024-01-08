#!/usr/bin/node
const [, , arg] = process.argv;
console.log(
  parseInt(parseInt(arg)) ? 'My number: ' + parseInt(arg) : 'Not a number'
);
