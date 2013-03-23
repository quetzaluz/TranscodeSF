
var WIDTH = 600;
var HEIGHT = 400;

var COLORS = [
  "red",  "orange", "yellow", "green",
  "blue", "indigo", "violet", "black"
];

var div_colors = document.getElementsByClassName("color");
var pen_color = "black"; //default pen color, can change.
var mouse_down = 0;
var last_x;
var last_y;

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


//Below is a helper function for the event listening scripts below.
function lastCoords(this_x, this_y) {
  last_x = this_x;
  last_y = this_y;
	}

function toolBarColors(e) {
  for (var color in COLORS) {
		div_colors[color].style.border = "5px solid white";}
  e.target.style.border = "5px solid cyan";
	pen_color = e.target.id;
	console.log("Pen color is now " + pen_color);
}

function startLine(e) {
	console.log("Start Pen Line at " + (e.x - e.target.offsetLeft) + "," + (e.y - e.target.offsetTop));
	mouse_down = 1;
	ctx.beginPath();
}

function linePath(e) {
	if(mouse_down === 0) {
		console.log("Not Drawing");}
	if(mouse_down === 1) {
		console.log("Drawing Pen Line.")
		var this_x = e.x - e.target.offsetLeft;
		var this_y = e.y - e.target.offsetTop;
		ctx.lineWidth = 3;
		ctx.strokeStyle = pen_color;
		ctx.beginPath();
		ctx.moveTo(last_x, last_y);
		ctx.lineTo(this_x, this_y);
		ctx.stroke();
		lastCoords(this_x, this_y);
	}
}

function endLine(e) {
	ctx.closePath();
	last_x = undefined;
	last_y = undefined;
	mouse_down = 0;
	console.log("Ending Pen Line");
}

window.addEventListener("load", init, false);
