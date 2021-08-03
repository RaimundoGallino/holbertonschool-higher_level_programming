#!/usr/bin/node

const list = require('./100-data.js').list;

console.log(list);

const map1 = list.map((x, i) => x * i);

console.log(map1);
