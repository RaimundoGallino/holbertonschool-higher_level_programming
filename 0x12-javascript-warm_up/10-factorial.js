#!/usr/bin/node

console.log(factorial(parseInt(process.argv[2])));

function factorial(n) {
    if (n > 1) {
        return n * factorial(n - 1);
    }
    return 1;
}
