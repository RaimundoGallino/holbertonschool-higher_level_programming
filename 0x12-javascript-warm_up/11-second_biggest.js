#!/usr/bin/node

const secondMax = function (arr) {
  const max = Math.max.apply(null, arr);
  const maxi = arr.indexOf(max);
  arr[maxi] = -Infinity;
  const secondMax = Math.max.apply(null, arr);
  arr[maxi] = max;
  return secondMax;
};

const num_array = process.argv.splice(2, process.argv.length);

num_array.map(function (item) {
  return parseInt(item, 10);
});

console.log(secondMax(num_array));
