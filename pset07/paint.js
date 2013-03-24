
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
	"pen", "rect_filled", "rect_outline", "eraser", "clear"
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
	canvas.addEventListener('mousedown', onMouseDown);
	canvas.addEventListener('mouseup', onMouseUp);
	canvas.addEventListener('mousemove', onMouseMove);
	canvas.addEventListener('mouseout', onMouseOut);
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
} //Try just offsetX and offsetY from e.

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
	if (tool_pick === "clear") { //This is the only tool called in toolbar
		clearTool(e);
	}
}

//The functions below handle tool behavior.
function penTool (click_stage, color_pick, e) {
	if (click_stage === "mouseDown"){
		console.log("Start Pen Line at " + (nowCoords('x', e)) + "," + (nowCoords('y', e)));
		ctx.beginPath();
	} else if(click_stage === "mouseMove"){
		console.log("Drawing Pen Line.")
		ctx.lineWidth = 3;
		ctx.strokeStyle = color_pick;
		ctx.beginPath();
		ctx.moveTo(last_x, last_y);
		ctx.lineTo(nowCoords('x', e), nowCoords('y', e));
		ctx.stroke();
		lastCoords(nowCoords('x', e), nowCoords('y', e));
	} else if(click_stage === "mouseUp"){
		ctx.closePath();
	}
}
function rectTool (click_stage, color_pick, e) {
	if (click_stage === "mouseDown") {
		rect_x1 = nowCoords('x', e);
		rect_y1 = nowCoords('y', e);
		console.log("Start Rectangle at " + nowCoords('x', e) + "," + nowCoords('y', e));
	} else if (click_stage === "mouseMove") {
	} else if (click_stage === "mouseUp") {
		rect_x2 = nowCoords('x', e);
		rect_y2 = nowCoords('y', e);
		rect_wid = Math.max(rect_x1, rect_x2) - Math.min (rect_x1, rect_x2);
		rect_hei = Math.max(rect_y1, rect_y2) - Math.min (rect_y1, rect_y2);
		rect_x = Math.min(rect_x1, rect_x2);
		rect_y = Math.min(rect_y1, rect_y2);
		if (tool_pick === "rect_filled") {
			ctx.fillStyle = color_pick;
			ctx.fillRect(rect_x, rect_y, rect_wid, rect_hei);
		} else if (tool_pick === "rect_outline") {
			ctx.strokeStyle = color_pick;
			ctx.lineWidth = 3;
			ctx.strokeRect(rect_x, rect_y, rect_wid, rect_hei);
		}
	}
}

function eraserTool (e) {
	//TODO: fill in later
}

function clearTool (e) {
	ctx.clearRect(0, 0, canvas.width, canvas.height);
		for (var tool in TOOLS) {
			div_tools[tool].style.border = "5px solid white";} 
		div_tools['pen'].style.border = "5px solid cyan";
		tool_pick = "pen";
}
//The three functions below enable click functionality on the canvas.
function onMouseDown(e) {
	mouse_down = 1;
	if (tool_pick === "pen") {
		penTool("mouseDown", color_pick, e);
	}else if (tool_pick === "rect_filled" || tool_pick === "rect_outline") {
		rectTool("mouseDown", color_pick, e);
	}
}

function onMouseMove(e) {
  this_x = nowCoords('x', e);
	this_y = nowCoords('y', e);
	if(mouse_down === 0) {
		console.log("Not Drawing");}
	if(mouse_down === 1) {
		if (tool_pick === "pen"){
			penTool("mouseMove", color_pick, e);
		}else if (tool_pick == "eraser") {
			console.log("Using Eraser")
		//  This was old code that cleared space in order to allow for transparency, but the result of this is spotty.
		//  ctx.clearRect((nowCoords('x', e) - 3), ((nowCoords('y', e) -3)), 6, 6);
		//	lastCoords(this_x, this_y);
		}
	}
}

function onMouseUp(e) {
	if (tool_pick === "pen") {
		penTool("mouseUp", color_pick, e);
	} else if (tool_pick === "rect_filled" || tool_pick === "rect_outline") {
		rectTool("mouseUp", color_pick, e);
		}
	last_x = undefined;
	last_y = undefined;
	mouse_down = 0;
	console.log("Ending Pen Line");
}

function onMouseOut(e) {
	mouse_down = 0;
	last_x = undefined;
	last_y = undefined;
	console.log("Off Canvas.")
}

window.addEventListener("load", init, false);
