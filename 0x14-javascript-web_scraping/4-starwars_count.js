#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request.get({ url: url }, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  let count = 0;
  const json = JSON.parse(body);
  json.results.forEach(element => {
    if (element.characters.includes('http://swapi.co/api/people/18/')) {
      count++;
    }
  });
  console.log(count);
});
