#!/usr/bin/node

const url = process.argv[2];
const path = process.argv[3];
const request = require('request');

request.get({ url: url }, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const fs = require('fs');

  fs.writeFile(path, body, 'utf8', (err) => {
    if (err) throw err;
  });
});
