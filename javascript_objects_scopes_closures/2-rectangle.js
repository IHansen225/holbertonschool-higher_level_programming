#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    let isValid = ((w > 0 || w !== undefined) && (h > 0 || h !== undefined));
    this.width = isValid ? w : undefined;
    this.height = isValid ? h : undefined;
  }
}
