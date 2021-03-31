const express = require("express");
const ejs = require("ejs");
const mongoose = require("mongoose");
const bodyParser = require("body-parser");

const app = express();

app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));

mongoose.connect("mongodb://localhost:27017/wikiDB", {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const articleSchema = {
  title: String,
  content: String,
};

const Article = mongoose.model("Article", articleSchema);

//Routes

//GET + READ - All articles
app.get("/articles", function (req, res) {
  Article.find({}, function (error, foundArticles) {
    if (!error) {
      res.send(foundArticles);
    } else {
      res.send(error);
    }
  });
});

//GET + READ - Specific article
app.get("/articles/:articleTitle", function (req, res) {
  Article.findOne(
    { title: req.params.articleTitle },
    function (error, foundArticle) {
      if (!error) {
        res.send(foundArticle);
      } else {
        res.send(error);
      }
    }
  );
});

// POST + CREATE - All articles
app.post("/articles", function (req, res) {
  const newArticle = new Article({
    title: req.body.title,
    content: req.body.content,
  });
  newArticle.save(function (error) {
    if (!err) {
      res.send("Successfully added a new article");
    } else {
      res.send(error);
    }
  });
});

//PUT + UPDATE - Specific article
app.put("/articles/:article", function (req, res) {
  Article.updateOne(
    { title: req.params.articleTitle },
    { title: req.body.title, content: req.body.title },
    { overwrite: true },
    function (error) {
      if (!error) {
        res.send("Successfully updated the article");
      } else {
        res.send(error);
      }
    }
  );
});

//PATCH + UPDATE - Specific article
app.patch("/articles/:articleTitle", function (req, res) {
  Article.updateOne(
    { title: req.params.articleTitle },
    { $set: req.body },
    function (error) {
      if (!error) {
        res.send("Successfully updated the article");
      } else {
        res.send(error);
      }
    }
  );
});

// DELETE + DELETE - All articles
app.delete("/articles", function (req, res) {
  Article.deleteMany({}, function (error) {
    if (!error) {
      res.send("Successfully deleted all articles");
    } else {
      res.send(error);
    }
  });
});

//DELETE + DELETE - Specific article
app.delete("/articles/:articleTitle", function (req, res) {
  Article.deleteOne({ title: req.params.articleTitle }, function (error) {
    if (!error) {
      res.send("Succesfully deleted the corresponding article");
    } else {
      res.send(error);
    }
  });
});

// Route Chaining - Refactoring code
// app
//   .route("/articles")
//   .get(function (req, res) {
//     Article.find({}, function (error, foundArticles) {
//       if (!error) {
//         res.send(foundArticles);
//       } else {
//         res.send(error);
//       }
//     });
//   })
//   .post(function (req, res) {
//     const newArticle = new Article({
//       title: req.body.title,
//       content: req.body.content,
//     });
//     newArticle.save(function (error) {
//       if (!err) {
//         res.send("Successfully added a new article");
//       } else {
//         res.send(error);
//       }
//     });
//   })
//   .delete(function (req, res) {
//     Article.deleteMany({}, function (error) {
//       if (!error) {
//         console.log("Successfully deleted all articles");
//       } else {
//         console.log(error);
//       }
//     });
//   });

//Server

app.listen(3000, function () {
  console.log("Server started on port 3000");
});
