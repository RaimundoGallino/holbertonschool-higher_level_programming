#!/usr/bin/node

if (process.argv[2] == null) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(process.argv[2]));
}
