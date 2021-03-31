let output = [];
let numCount = 1;
let numEnd = prompt("What length of FizzBuzz do you want?");
function fizzBuzz() {
  while (numCount <= numEnd) {
    if (numCount % 3 === 0 && numCount % 5 === 0) {
      output.push("FizzBuzz");
    } else if (numCount % 3 === 0) {
      output.push("Fizz");
    } else if (numCount % 5 === 0) {
      output.push("Buzz");
    } else {
      output.push(numCount);
    }
    numCount++;
  }
}
