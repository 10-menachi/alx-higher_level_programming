#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
const string_to_write = process.argv[3];

fs.writeFile(file, string_to_write, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
    return;
  }
});
