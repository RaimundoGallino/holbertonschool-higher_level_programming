#!/usr/bin/node

if (isNaN(parseInt(process.argv[2]))) {
    console.log('Missing size');
}
else {
    const n_ocurr = process.argv[2];
    for (let i = 0; i < n_ocurr; i++) {
            console.log('X'.repeat(n_ocurr));
    }
}
