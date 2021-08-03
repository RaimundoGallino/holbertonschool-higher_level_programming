#!/usr/bin/node

class Rectangle {
  constructor (h, w) {
    if (w > 0 && h > 0) {
      this.height = h;
      this.width = w;
    }
  }
}
module.exports = Rectangle;
