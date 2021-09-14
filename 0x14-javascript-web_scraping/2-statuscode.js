#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request.get({ url: url }, function (err, res, user) {
  if (err) {
    console.log(err);
  }
  console.log('code: ' + res.statusCode);
});
