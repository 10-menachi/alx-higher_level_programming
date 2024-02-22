#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    let users = JSON.parse(body);
    let completed = {};
    users.reduce(function (acc, user) {
      if (user.completed) {
        if (acc[user.userId]) {
          acc[user.userId] += 1;
        } else {
          acc[user.userId] = 1;
        }
      }
      return acc;
    }, completed);
    console.log(completed);
  }
});
