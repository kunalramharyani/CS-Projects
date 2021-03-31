const express = require("express");
const bodyParser = require("body-parser");

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));

// Routes
app.get("/", function (req, resp) {
  resp.sendFile(__dirname + "/index.html");
});

app.post("/", function (req, resp) {
  let num1 = Number(req.body.num1);
  let num2 = Number(req.body.num2);
  let operator = req.body.operator;
  let result;
  switch (operator) {
    case "+":
      result = num1 + num2;
      break;
    case "-":
      result = num1 - num2;
      break;
    case "*":
      result = num1 * num2;
      break;
    case "/":
      result = num1 / num2;
      break;
    case "^":
      result = Math.pow(num1, num2);
      break;
    default:
      result = "not possible, please use a valid operator (+, -, *, /, ^).";
  }
  resp.send("The result of the calculation is " + result);
});

app.get("/bmicalculator", function (req, resp) {
  resp.sendFile(__dirname + "/bmiCalculator.html");
});

app.post("/bmicalculator", function (req, resp) {
  let weight = parseFloat(req.body.weight);
  let height = parseFloat(req.body.height);
  let bmi = weight / Math.pow(height, 2);
  resp.send("Your BMI is " + bmi);
});

// Server
app.listen(3000, function () {
  console.log("Server started on port 3000");
});
