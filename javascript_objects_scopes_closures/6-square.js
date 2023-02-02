#!/usr/bin/node
const Base = require('./5-square');

class Square extends Base {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      console.log((c || 'X').repeat(this.width));
    }
  }
}

module.exports = Square;
