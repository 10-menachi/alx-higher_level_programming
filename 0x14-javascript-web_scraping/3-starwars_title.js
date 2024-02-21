#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url).on('response', function (response) {
  const title = JSON.parse(response.body).title;
  console.log(title);
});
