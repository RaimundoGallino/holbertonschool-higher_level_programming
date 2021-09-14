#!/usr/bin/node

const path = process.argv[2];
const fs = require('fs');

fs.readFile(path, 'utf8', function (err, data) {
    if (err) {
        console.log(err);
        return;
    }
    console.log(data);

});
