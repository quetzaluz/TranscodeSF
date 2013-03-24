
var WIDTH = 600;
var HEIGHT = 400;
var canvas;
var ctx;
var div_colors = document.getElementsByClassName("color");
var div_tools = document.getElementsByClassName("tool");
var color_pick = "black"; //default tool color, can change.
var tool_pick = "pen"; //default tool is pen
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
	"pen", "rect", "eraser", "clear"
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
	}
	for (var tool in TOOLS) {
		div_tools[tool].addEventListener("click", toolBarTools);
		div_tools[tool].style.border = "5px solid white";
	}
	div_colors['black'].style.border = "5px solid cyan";
	div_tools['pen'].style.border = "5px solid cyan";
	canvas.addEventListener('mousedown', startLine);
	canvas.addEventListener('mouseup', endLine);
	canvas.addEventListener('mousemove', linePath);
	canvas.addEventListener('mouseout', offCanvas);
}


//Below are two helper functions for the event listening scripts below.
function lastCoords(this_x, this_y) {
  last_x = this_x;
  last_y = this_y;
	}

function nowCoords(x_or_y, e) {
	if (x_or_y === 'x') {
		return e.clientX + document.body.scrollLeft - e.target.offsetLeft;
	}
	if (x_or_y === 'y') {
		return e.clientY + document.body.scrollTop - e.target.offsetTop;
	}
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
	color_pick = e.target.id;
	console.log("Tool color is now " + color_pick);
}

function toolBarTools(e) {
	for (var tool in TOOLS) {
		div_tools[tool].style.border = "5px solid white";}
	e.target.style.border = "5px solid cyan";
	tool_pick = e.target.id;
	console.log("Tool selected is now " + tool_pick);
	if (tool_pick === "clear") { //This is the only tool called this way--others will be called in the functions below.
		ctx.clearRect(0, 0, canvas.width, canvas.height);
	}
}

function startLine(e) {
	mouse_down = 1;
	if (tool_pick === "pen") {
		console.log("Start Pen Line at " + (nowCoords('x', e)) + "," + (nowCoords('y', e)));
		ctx.beginPath();
	}else if (tool_pick === "rect") {
		rect_x1 = nowCoords('x', e);
		rect_y1 = nowCoords('y', e);
		console.log("Start Rectangle at " + nowCoords('x', e) + "," + nowCoords('y', e));
	}
}

function linePath(e) {
  this_x = nowCoords('x', e);
	this_y = nowCoords('y', e);
	if(mouse_down === 0) {
		console.log("Not Drawing");}
	if(mouse_down === 1) {
		if (tool_pick === "pen"){
			console.log("Drawing Pen Line.")
			ctx.lineWidth = 3;
			ctx.strokeStyle = color_pick;
			ctx.beginPath();
			ctx.moveTo(last_x, last_y);
			ctx.lineTo(this_x, this_y);
			ctx.stroke();
			lastCoords(this_x, this_y);
		}else if (tool_pick === "rect") {
			console.log("Drawing Rectangle")
		}else if (tool_pick === "clear") {
			tool_pick = "pen";
		}
	}
}

function endLine(e) {
	if (tool_pick === "pen") {
		ctx.closePath();
	} else if (tool_pick === "rect") {
		rect_x2 = nowCoords('x', e);
		rect_y2 = nowCoords('y', e);
		rect_wid = rect_x2 - rect_x1;
		rect_hei = rect_y2 - rect_y1;
		if (rect_wid < 0) {
			rect_wid = rect_wid * -1;
		}
		if (rect_hei < 0) {
			rect_hei = rect_hei * -1;
		}
		if (rect_x1 < rect_x2 && rect_y1 > rect_y2) {
			rect_y1 = rect_y2;
		} else if (rect_x1 > rect_x2 && rect_y1 > rect_y2) {
			rect_x1 = rect_x2;
			rect_y1 = rect_y2;
		} else if (rect_x1 > rect_x2 && rect_y1 < rect_y2) {
			rect_x1 = rect_x2;
		}
		ctx.fillStyle = color_pick;
		ctx.fillRect(rect_x1, rect_y1, rect_wid, rect_hei);
	}
	last_x = undefined;
	last_y = undefined;
	mouse_down = 0;
	console.log("Ending Pen Line");
}

window.addEventListener("load", init, false);
