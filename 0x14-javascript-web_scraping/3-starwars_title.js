#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request.get({ url: url }, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const json = JSON.parse(body);
  console.log(json.title);
});
