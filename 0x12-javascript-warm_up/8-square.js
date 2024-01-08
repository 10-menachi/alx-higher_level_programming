#!/usr/bin/node
const [, , arg] = process.argv;
if (parseInt(arg)) {
  for (let i = 0; i < parseInt(arg); i++) {
    console.log('X'.repeat(parseInt(arg)));
  }
} else {
  console.log('Missing size');
}
