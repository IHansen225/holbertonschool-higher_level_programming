#!/usr/bin/node
const Square = require('./5-square');

module.exports = class Square extends Square {
  constructor (size) {
    super(size, size);
  }

  charprint (c) {
    if (c === undefined) {
      this.print();
      return;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
