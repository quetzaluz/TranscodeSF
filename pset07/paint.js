
var WIDTH = 600;
var HEIGHT = 400;
var canvas;
var ctx;
var div_colors = document.getElementsByClassName("color");
var pen_color = "black"; //default pen color, can change.
var mouse_down = 0;
var this_x;
var this_y;
var last_x;
var last_y;

var COLORS = [
  "red",  "orange", "yellow", "green",
  "blue", "indigo", "violet", "black"
];

var TOOLS = [
	"pen", "rectangle"
];

function each(obj, f) {
  for (var key in obj) {
    if (obj.hasOwnProperty(key)) {
      f(obj[key], key);
    }
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
	div_colors['black'].style.border = "5px solid cyan";
	canvas.addEventListener('mousedown', startLine);
	canvas.addEventListener('mouseup', endLine);
	canvas.addEventListener('mousemove', linePath);
	canvas.addEventListener('mouseout', offCanvas);
	}
}


//Below is a helper function for the event listening scripts below.
function lastCoords(this_x, this_y) {
  last_x = this_x;
  last_y = this_y;
	}

function offCanvas(e) {
	mouse_down = 0;
	last_x = undefined;
	last_y = undefined;
	console.log("Off Canvas.")
}

function toolBarColors(e) {
	for (var color in COLORS) {
		div_colors[color].style.border = "5px solid white";} 
	e.target.style.border = "5px solid cyan";
	pen_color = e.target.id;
	console.log("Pen color is now " + pen_color);
}

function startLine(e) {
	console.log("Start Pen Line at " + (e.clientX + document.body.scrollLeft - e.target.offsetLeft) + "," + (e.clientY + document.body.scrollTop - e.target.offsetTop));
	mouse_down = 1;
	ctx.beginPath();
}

function linePath(e) {
  this_x = e.clientX + document.body.scrollLeft - e.target.offsetLeft;
	this_y = e.clientY + document.body.scrollTop - e.target.offsetTop;
	if(mouse_down === 0) {
		console.log("Not Drawing");}
	if(mouse_down === 1) {
		e.preventDefault(); // Try to avoid error where dragging highlights elements.
		console.log("Drawing Pen Line.")
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
