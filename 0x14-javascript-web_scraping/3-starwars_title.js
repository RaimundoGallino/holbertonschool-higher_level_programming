#!/usr/bin/node

const id = process.argv[2];
const request = require('request');

request.get({ url: `https://swapi-api.hbtn.io/api/films/${id}` }, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const json = JSON.parse(body);
  console.log(json.title);
});
