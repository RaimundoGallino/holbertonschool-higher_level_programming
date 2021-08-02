#!/usr/bin/node

if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  const nOcurr = process.argv[2];
  for (let i = 0; i < nOcurr; i++) {
    console.log('C is fun');
  }
}
