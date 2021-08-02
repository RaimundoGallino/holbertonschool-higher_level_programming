#!/usr/bin/node

if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  const nOcurr = process.argv[2];
  for (let i = 0; i < nOcurr; i++) {
    console.log('X'.repeat(nOcurr));
  }
}
