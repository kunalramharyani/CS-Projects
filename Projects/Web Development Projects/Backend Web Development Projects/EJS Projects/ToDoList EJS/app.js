const express = require("express");
const bodyParser = require("body-parser");
const ejs = require("ejs");
const date = require(__dirname + "/date.js");

const app = express();
const day = date.getDate();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));
app.set("view engine", "ejs");

const items = [];
const workListItems = [];
const port = process.env.PORT || 3000;

// Routes
app.get("/", function (req, res) {
  res.render("list", { listTitle: day, newListItems: items });
});

app.post("/", function (req, res) {
  const item = req.body.newItem;
  if (req.body.list === "Work List") {
    workListItems.push(item);
    res.redirect("/work");
  } else {
    items.push(item);
    res.redirect("/");
  }
});

app.get("/work", function (req, res) {
  res.render("list", { listTitle: "Work List", newListItems: workListItems });
});

app.post("/work", function (req, res) {
  res.redirect("/work");
});

app.get("/about", function (req, res) {
  res.render("about");
});

//Server start
app.listen(port, function () {
  console.log("Server started sucessfully");
});
