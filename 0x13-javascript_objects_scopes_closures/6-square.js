#!/usr/bin/node

const SquareX = require('./5-square');

class Square extends SquareX {
  constructor (size) {
    super(size, size);
  }

  charPrint (char) {
    if (char === undefined) {
      char = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(char.repeat(this.height));
    }
  }
}
module.exports = Square;
