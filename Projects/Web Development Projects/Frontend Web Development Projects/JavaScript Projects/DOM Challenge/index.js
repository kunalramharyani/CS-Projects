// Changing inner HTML
document.querySelectorAll(".list")[2].innerHTML =
  "This item's text was changed by JS.";

// Changing styles. Do not do this, makes debugging harder
document.querySelector("ul li a").style.color = "red";
document.querySelector("button").style.backgroundColor = "yellow";

// Changing text content
document.querySelector("h1").textContent = "Hello, World!";

// Changing attributes
document.querySelector("a").setAttribute("href", "https://www.bing.com");

// Separation of Concern
document.querySelector("h1").classList.add("huge");
