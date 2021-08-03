#!/usr/bin/node

class Rectangle {
    constructor(h, w) {
        if (w > 0 && h > 0) {
            this.height = h;
            this.width = w;
        }
    }
    print () {
        for (let i = 0; i < this.width; i++) {
            console.log('X'.repeat(this.height));
        }
    }
    rotate () {
        const aux = this.height;
        this.height = this.width;
        this.width = aux;
    }
    double () {
        this.height *= 2;
        this.width *= 2;
    }
}
module.exports = Rectangle;
