
var WIDTH = 600;
var HEIGHT = 400;

var COLORS = [
  "red",  "orange", "yellow", "green",
  "blue", "indigo", "violet", "black"
];

var div_colors = document.getElementsByClassName("color");

// Globals for this file
var canvas;
var ctx;

function each(obj, f) {
  for (var key in obj) {
    if (obj.hasOwnProperty(key)) {
      f(obj[key], key);
q    }
  }
};

function init() {
  canvas = document.getElementById("paint");
  canvas.width = WIDTH;
  canvas.height = HEIGHT;
  ctx = canvas.getContext('2d'); 
  for (var color in COLORS) {
	div_colors[color].addEventListener("click", toolBarColors);
	div_colors[color].style.border = "5px solid grey";
  }}

function toolBarColors(e) {
  for (var color in COLORS) {
	div_colors[color].style.border = "5px solid grey";}
	console.log("You clicked " + e.target.id); //will delete later
	e.target.style.border = "5px solid cyan";
}

window.addEventListener("load", init, false);
