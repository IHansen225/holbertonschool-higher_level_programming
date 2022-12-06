#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    const invalid = ((w < 0 || w === undefined) || (h < 0 || h === undefined));
    if (!invalid) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
};
