#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    const isValid = ((w < 0 || w !== undefined) && (h < 0 || h !== undefined));
    if (isValid) {
      this.width = isValid ? w : undefined;
      this.height = isValid ? h : undefined;
    }
  }
};
