function isLeap(year) {
  if (year % 4 === 0) {
    if (year % 100 !== 0) {
      return "Leap year.";
    } else if (year % 100 === 0) {
      if (year % 400 === 0) {
        return "Leap year.";
      } else if (year % 400 !== 0) {
        return "Not leap year.";
      }
    }
  } else {
    return "Not leap year.";
  }
}
