function whosPaying(names) {
  let randomNum = Math.random();
  let randomNumFloor = Math.floor(randomNum * names.length);
  let randomName = names[randomNumFloor];
  return randomName + " is going to buy lunch today!";
}
