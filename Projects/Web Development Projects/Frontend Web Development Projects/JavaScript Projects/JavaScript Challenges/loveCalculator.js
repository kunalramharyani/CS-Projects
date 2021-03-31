function loveCalculator() {
  alert("Welcome to the love score calculator");
  prompt("What is your name?");
  prompt("What is their name?");
  let loveScore = Math.random() * 100;
  loveScore = Math.floor(loveScore) + 1;
  if (loveScore > 70) {
    alert(
      "Your love score is " + loveScore + "%" + "You love each other a lot!"
    );
  }
  if (loveScore > 30 && loveScore <= 70) {
    alert("Your love score is " + loveScore + "%");
  }
  if (loveScore <= 30) {
    alert(
      "Your love score is " +
        loveScore +
        "%" +
        "You go together like oil and water."
    );
  }
}
