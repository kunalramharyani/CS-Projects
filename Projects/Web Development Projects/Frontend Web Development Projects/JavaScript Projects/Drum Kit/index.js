let drumButtons = document.querySelectorAll(".drum");
let numberOfDrumButtons = drumButtons.length;
let acceptedButtons = [
  "w",
  "a",
  "s",
  "d",
  "j",
  "k",
  "l",
  "W",
  "A",
  "S",
  "D",
  "J",
  "K",
  "L",
];

for (let i = 0; i < numberOfDrumButtons; i++) {
  drumButtons[i].addEventListener("click", (event) => {
    playSound(event.target.innerText);
    buttonAnimation(event.target.innerText);
  });
}

document.addEventListener("keydown", (event) => {
  playSound(event.key);
  buttonAnimation(event.key);
});

function playSound(keyButton) {
  let sound = "";
  if (acceptedButtons.includes(keyButton)) {
    switch (keyButton) {
      case "w":
      case "W":
        sound = "tom-1.mp3";
        break;
      case "a":
      case "A":
        sound = "tom-2.mp3";
        break;
      case "s":
      case "S":
        sound = "tom-3.mp3";
        break;
      case "d":
      case "D":
        sound = "tom-4.mp3";
        break;
      case "j":
      case "J":
        sound = "snare.mp3";
        break;
      case "k":
      case "K":
        sound = "crash.mp3";
        break;
      case "l":
      case "L":
        sound = "kick-bass.mp3";
        break;
      default:
        sound = false;
    }
    if (sound) {
      let audio = new Audio("sounds/" + sound);
      audio.play();
    }
  }
}

function buttonAnimation(keyButton) {
  if (acceptedButtons.includes(keyButton)) {
    let pressedButton = document.querySelector("." + keyButton.toLowerCase());
    pressedButton.classList.add("pressed");
    setTimeout(() => {
      pressedButton.classList.remove("pressed");
    }, 100);
  }
}
