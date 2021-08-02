#!/usr/bin/node

let secondMax = function (arr) { 
    let max = Math.max.apply(null, arr);
    let maxi = arr.indexOf(max);
    arr[maxi] = -Infinity;
    let secondMax = Math.max.apply(null, arr);
    arr[maxi] = max;
    return secondMax;
};

const num_array = process.argv.splice(2, process.argv.length);

num_array.map(function (item) {
    return parseInt(item, 10)
});


console.log(secondMax(num_array));

