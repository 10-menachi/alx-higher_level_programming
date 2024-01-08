#!/usr/bin/node
const [, arg] = process.argv;
if (arg) {
  console.log(args[0]);
} else {
  console.log('No argument');
}
