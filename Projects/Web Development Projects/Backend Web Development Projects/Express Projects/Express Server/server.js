const express = require("express");
const app = express();

// Routes
app.get("/", function (request, response) {
  response.send("Hello!");
});

app.get("/contact", function (request, response) {
  response.send("Contact me at: kunalharyani@gmail.com");
});

app.get("/about", function (request, response) {
  response.send("My name is Kunal Haryani and I am a CS student.");
});

app.get("/hobbies", function (request, response) {
  response.send("I love to read, skate and play videogames");
});

// Server start
app.listen(3000, function () {
  console.log("Server started on port 3000");
});
