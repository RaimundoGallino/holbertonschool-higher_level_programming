#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
const dict = {};

request.get({ url: url }, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const json = JSON.parse(body);
    json.forEach(element => {
      const key = element.userId;
      if (element.completed === true) {
        if (!(key in dict)) {
          dict[key] = 1;
        } else {
          dict[key] += 1;
        }
      }
    });
    console.log(dict);
  }
});
