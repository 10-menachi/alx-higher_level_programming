#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    console.log(
      JSON.parse(body).results.filter((element) => {
        return (
          element.characters.filter((character) => character.includes('18'))
            .length > 0
        );
      })
    );
  }
});
