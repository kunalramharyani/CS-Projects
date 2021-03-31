// Adding a class and changing text
$("h1").addClass("big-title-yellow margin-50").text("Hello There.");

// Changing attributes
$("a").attr("href", "https://www.bing.com");

// Adding event listeners
$("h1").click(() => {
  $("h1").removeClass("big-title-yellow big-title-green");
  $("h1").addClass("big-title-purple");
});

$("button").click(() => {
  $("button").text("You clicked us!");
});

$("input").keydown((event) => {
  console.log(event.key);
});

// $(document).keydown((event) => {
//     $("h1").text(event.key)
// });

$(document).on("wheel", () => {
  $("h1").removeClass("big-title-yellow big-title-purple");
  $("h1").addClass("big-title-green");
});

//Adding and removing elements
// $("h1").before("<button>New</button>");
// $("h1").after("<button>New</button>");
// $("h1").prepend("<button>New</button>");
// $("h1").append("<button>New</button>");

//Adding animations
// $("h1").hide();
// $("h1").show();
// $("h1").fadeIn();
// $("h1").fadeOut();
// $("h1").slideUp();
// $("h1").slideDown();
// $("h1").animate({margin: "20%"});
