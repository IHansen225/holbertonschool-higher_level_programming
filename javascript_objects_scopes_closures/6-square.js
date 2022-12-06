#!/usr/bin/node
const Square = require('./5-square.js');

module.exports = class Square extends Square {
  constructor (size) {
    super(size, size);
  }

  charprint (c) {
    c = (c === undefined) ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
