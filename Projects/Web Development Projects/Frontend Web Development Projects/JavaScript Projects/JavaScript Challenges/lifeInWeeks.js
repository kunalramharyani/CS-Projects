function lifeInWeeks(age) {
  /************Don't change the code above************/

  //Write your code here.
  var remainderAge = 90 - age;
  var days = remainderAge * 365;
  var weeks = remainderAge * 52;
  var months = remainderAge * 12;
  console.log(
    "You have " +
      days +
      " days, " +
      weeks +
      " weeks, and " +
      months +
      " months left."
  );

  /*************Don't change the code below**********/
}
