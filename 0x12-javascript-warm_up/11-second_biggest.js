#!/usr/bin/node

const secondMax = function (arr) {
  const max = Math.max.apply(null, arr);
  const maxi = arr.indexOf(max);
  arr[maxi] = -Infinity;
  const secondMax = Math.max.apply(null, arr);
  arr[maxi] = max;
  return secondMax;
};

const numArr = process.argv.splice(2, process.argv.length);

numArr.map(function (item) {
  return parseInt(item, 10);
});

console.log(secondMax(numArr));
