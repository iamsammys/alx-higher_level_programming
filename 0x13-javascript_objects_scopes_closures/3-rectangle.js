#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let newStr = '';
      for (let j = 0; j < this.width; j++) {
        newStr += 'X';
      }
      console.log(newStr);
    }
  }
}
module.exports = Rectangle;
