#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
    constructor(size) {
        super(size, size);
    }
    charPrint (char) {
        for (let i = 0; i < this.width; i++) {
            console.log(char.repeat(this.height));
        }
    }
}
module.exports = Square;
