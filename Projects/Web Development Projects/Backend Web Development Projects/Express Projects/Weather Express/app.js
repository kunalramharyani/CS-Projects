const express = require("express");
const https = require("https");
const bodyParser = require("body-parser");
const app = express();

app.use(bodyParser.urlencoded({ extended: true }));

// Routes
app.get("/", function (req, res) {
  res.sendFile(__dirname + "/index.html");
});

app.post("/", function (req, res) {
  const cityQuery = req.body.cityName;
  const apiKey = process.env.API_KEY;
  const units = "metric";
  const url =
    "https://api.openweathermap.org/data/2.5/weather?q=" +
    cityQuery +
    "&units=" +
    units +
    "&appid=" +
    apiKey;
  https.get(url, function (resp) {
    console.log(resp.statusCode);
    resp.on("data", function (data) {
      const weatherData = JSON.parse(data);
      const temp = weatherData.main.temp;
      const weatherDescription = weatherData.weather[0].description;
      const icon = weatherData.weather[0].icon;
      const imageURL = "https://openweathermap.org/img/wn/" + icon + "@2x.png";
      res.write(
        "<h1>The temperature in " +
          cityQuery +
          " is " +
          temp +
          " degrees Celcius.</h1>"
      );
      res.write("<p>The weather is currently " + weatherDescription + "</p>");
      res.write("<img src =" + imageURL + ">");
      res.send();
    });
  });
});

// Server start
app.listen(3000, function (params) {
  console.log("Server is running on port 3000.");
});
