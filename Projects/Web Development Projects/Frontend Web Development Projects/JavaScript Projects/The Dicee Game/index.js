let randomNumber1 = Math.floor(Math.random() * 6) + 1;
let imageSource1 = "images/dice" + randomNumber1 + ".png";
document.querySelectorAll("img")[0].setAttribute("src", imageSource1);

let randomNumber2 = Math.floor(Math.random() * 6) + 1;
let imageSource2 = "images/dice" + randomNumber2 + ".png";
document.querySelectorAll("img")[1].setAttribute("src", imageSource2);

let winnerText = "";
if (randomNumber1 > randomNumber2) {
  winnerText = "🚩 Player 1 won!";
} else if (randomNumber2 > randomNumber1) {
  winnerText = "Player 2 won! 🚩";
} else {
  winnerText = "Draw!";
}

document.querySelector("h1").innerHTML = winnerText;
