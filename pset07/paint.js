
var WIDTH = 600;
var HEIGHT = 400;

var COLORS = [
  "red",  "orange", "yellow", "green",
  "blue", "indigo", "violet", "black"
];

var div_colors = document.getElementsByClassName("color");
var pen_color = "black"; //default pen color, can change.
var mouse_down = 0;

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
		div_colors[color].style.border = "5px solid white";
	canvas.addEventListener('mousedown', startLine);
	canvas.addEventListener('mouseup', endLine);
	canvas.addEventListener('mousemove', linePath);
}}


function toolBarColors(e) {
  for (var color in COLORS) {
		div_colors[color].style.border = "5px solid white";}
  e.target.style.border = "5px solid cyan";
	pen_color = e.target.id
	console.log("Pen color is now " + pen_color)
}

function startLine(e) {
	console.log("Start Pen Line at " + (e.x - e.target.offsetLeft) + "," + (e.y - e.target.offsetTop));
	mouse_down = 1;
}

function linePath(e) {
	if(mouse_down === 0) {
		console.log("Not Drawing")}
	if(mouse_down === 1) {
		console.log("Drawing Pen Line.")
		var mouse_x = e.x - e.target.offsetLeft
		var mouse_y = e.y - e.target.offsetTop
		ctx.beginPath();
		ctx.moveTo(mouse_x, mouse_y);
		ctx.arc(mouse_x, mouse_y, 3, Math.PI*2, true)
		ctx.fillStyle = pen_color;
		ctx.fill();
	}
}

function endLine(e) {

	mouse_down = 0;
	console.log("Ending Pen Line");
}

window.addEventListener("load", init, false);
