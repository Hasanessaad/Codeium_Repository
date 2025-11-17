function SimpleCalc() {
  this.sum = function(a, b) {
    return a + b;
  }
  this.sub = function(a, b) {
    return a - b;
  }
  this.mul = function(a, b) {
    return a * b;
  }
  this.div = function(a, b) {
    if (b === 0) {
      throw new Error("Cannot divide by zero");
    }
    return a / b;
  }
}
