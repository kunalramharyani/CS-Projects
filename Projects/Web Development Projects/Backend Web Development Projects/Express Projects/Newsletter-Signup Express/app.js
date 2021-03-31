require("dotenv").config();
const express = require("express");
const bodyParser = require("body-parser");
const https = require("https");
const { default: merge } = require("utils-merge");
const app = express();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));

//Routes
app.get("/", function (req, res) {
  res.sendFile(__dirname + "/views/signup.html");
});

app.post("/", function (req, res) {
  const firstName = req.body.fName;
  const lastName = req.body.lName;
  const email = req.body.email;
  const data = {
    members: [
      {
        email_address: email,
        status: "subscribed",
        merge_fields: {
          FNAME: firstName,
          LNAME: lastName,
        },
      },
    ],
  };

  const jsonData = JSON.stringify(data);

  const options = {
    method: "POST",
    auth: process.env.AUTH,
  };

  const request = https.request(process.env.URL, options, function (response) {
    if (response.statusCode === 200) {
      res.sendFile(__dirname + "/views/success.html");
    } else {
      res.sendFile(__dirname + "/views/failure.html");
    }
    response.on("data", function (data) {
      console.log(JSON.parse(data));
    });
  });
  request.write(jsonData);
  request.end();
});

app.post("/views/failure", function (req, res) {
  res.redirect("/");
});

// Server
app.listen(process.env.PORT || 3000, function () {
  console.log("Server is listening on local port 3000.");
});
