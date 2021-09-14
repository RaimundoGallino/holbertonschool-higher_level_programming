#!/usr/bin/node

const path = process.argv[2];
const text = process.argv[3];
const fs = require('fs');

fs.writeFile(path, text, (err) => {
  if (err) throw err;
});
