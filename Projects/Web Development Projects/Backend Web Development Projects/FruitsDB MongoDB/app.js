const mongoose = require("mongoose");

mongoose.connect("mongodb://localhost:27017/fruitsDB", {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const fruitSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  rating: {
    type: Number,
    min: 1,
    max: 10,
  },
  review: String,
});

const Fruit = mongoose.model("Fruit", fruitSchema);

peach.save().catch((e) => {
  if (e) {
    console.log(`Coud not save Peach\n${e}`);
  }
});

Fruit.find(function (err, fruits) {
  if (err) {
    console.log(`ERROR: ${err}`);
  } else {
    // console.log(`Fruits:\n ${fruits}');
    console.log(`Found ${fruits.length} fruits in collection`);
    fruits.forEach((fruit) => {
      console.log(fruit.name);
    });
  }
});

Fruit.updateOne(
  {
    name: "Peach",
  },
  {
    rating: 9,
  },
  (e) => {
    if (e) {
      console.log(`Error updating Peach ${e}`);
    } else {
      console.log("Updated Peach record");
    }
  }
);

Fruit.deleteMany(
  {
    name: "Peach",
  },
  function (e, res) {
    if (e) {
      console.log(`Error deleting Peach ${e}`);
    } else {
      console.log(`Succesfully deleted ${res.deletedCount} Peach`);
    }
  }
);

// mongoose.connection.close();

Fruit.deleteMany(
  {
    _id: {
      $exists: 1,
    },
  },
  function (err) {
    if (err) {
      console.log(err);
    }
  }
);

const fruit = new Fruit({
  name: "Apple",
  rating: 7,
  review: "Pretty solid as a fruit.",
});

//fruit.save();

const kiwi = new Fruit({
  name: "Kiwi",
  score: 10,
  review: "The best fruit",
});

const orange = new Fruit({
  name: "Orange",
  score: 4,
  review: "Too sour for me",
});

const banana = new Fruit({
  name: "Banana",
  score: 3,
  review: "Weird texture",
});

Fruit.insertMany([kiwi, orange, banana], function (err) {
  if (err) {
    console.log(`ERROR: ${err}`);
  } else {
    console.log("Successfully saved fruits to db");
  }
});
