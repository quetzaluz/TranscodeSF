
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

var tool_handler = {
  "pen": {
    "mousedown": penMouseDown,
    "mousemove": penMouseMove,
    "mouseup": penMouseUp
  },
  "rect_filled": {
		"mousedown": rectMouseDown,
		"mouseup": rectMouseUp
	},
	"rect_outline": {
		"mousedown": rectMouseDown,
		"mouseup": rectMouseUp
	},
	"eraser": {
		"mousedown": eraserMouseDown,
		"mousemove": eraserMouseMove,
		"mouseup": eraserMouseUp
	}
};

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
		div_colors[color].className += " no_highlight";
	}
	for (var tool in TOOLS) {
		div_tools[tool].addEventListener("click", toolBarTools);
		div_tools[tool].className += " no_highlight";
	}
	div_colors['black'].className = div_colors['black'].className.replace( /(?:^|\s)no_highlight(?!\S)/g , '' );
	div_colors['black'].className += " highlight";
	div_tools['pen'].className = div_tools['pen'].className.replace
      ( /(?:^|\s)no_highlight(?!\S)/g , '' );
	div_tools['pen'].className += " highlight";
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

function nowCoordX(e) {
	return e.offsetX;
}

function nowCoordY(e) {
	return e.offsetY;
}

//Below is a helper function for clearing existing toolbar element highlights. This is called before changing highlight classes.

function clearHighlights(e) {
	e.className = e.className.replace(/(?:^|\s)highlight(?!\S)/g , '' );
	e.className = e.className.replace(/(?:^|\s)no_highlight(?!\S)/g , '' );
}

function toolBarColors(e) {
	for (var color in COLORS) {
		clearHighlights(div_colors[color]);
		div_colors[color].className += " no_highlight";} 
	clearHighlights(e.target);
	e.target.className += " highlight";
	color_pick = e.target.id;
	console.log("Tool color is now " + color_pick);
}

function toolBarTools(e) {
	for (var tool in TOOLS) {
		clearHighlights(div_tools[tool]);
		div_tools[tool].className += " no_highlight";}
	clearHighlights(e.target);
	e.target.className += " highlight";
	tool_pick = e.target.id;
	console.log("Tool selected is now " + tool_pick);
	if (tool_pick === "clear") { //This is the only tool called in toolbar
		clearTool(e);
	}
}

//The functions below handle tool behavior.

function penMouseDown (e, color_pick) {
	console.log("Start Pen Line at " + (nowCoordX(e)) + "," + (nowCoordY(e)));
	ctx.beginPath();
}

function penMouseMove (e, color_pick) {
	console.log("Drawing Pen Line.")
	ctx.lineWidth = 3;
	ctx.strokeStyle = color_pick;
	ctx.beginPath();
	ctx.moveTo(last_x, last_y);
	ctx.lineTo(nowCoordX(e), nowCoordY(e));
	ctx.stroke();
	lastCoords(nowCoordX(e), nowCoordY(e));
}

function penMouseUp (e, color_pick) {
	ctx.closePath();
}

function rectMouseDown (e, color_pick) {
	rect_x1 = nowCoordX(e);
	rect_y1 = nowCoordY(e);
	console.log("Start Rectangle at " + nowCoordX(e) + "," + nowCoordY(e));
}

function rectMouseUp (e, color_pick) {
	rect_x2 = nowCoordX(e);
	rect_y2 = nowCoordY(e);
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

function eraserMouseDown (e, color_pick) {
	penMouseDown(e, color_pick);
}

function eraserMouseMove (e, color_pick) {
	old_color = color_pick;
	color_pick = 'white';
	penMouseMove(e, color_pick);
}

function eraserMouseUp (e, color_pick) {
	penMouseUp(e, color_pick);
	color_pick = old_color;
	old_color = "undefined";
}

		//  This was old code that cleared space in order to allow for transparency, but the result of this is spotty.
		//  ctx.clearRect((nowCoords('x', e) - 3), ((nowCoords('y', e) -3)), 6, 6);
		//	lastCoords(this_x, this_y);

function clearTool (e) {
	ctx.clearRect(0, 0, canvas.width, canvas.height);
		for (var tool in TOOLS) {
			clearHighlights(div_tools[tool]);} 
		div_tools['pen'].className += " highlight";
		tool_pick = "pen";
}

//The three functions below enable click functionality on the canvas.
function onMouseDown(e) {
	mouse_down = 1;
	tool_handler[tool_pick]['mousedown'](e, color_pick);
}

function onMouseMove(e) {
  this_x = nowCoordX(e);
	this_y = nowCoordY(e);
	if(mouse_down === 0) {
		console.log("Not Drawing");}
	if(mouse_down === 1) {
		tool_handler[tool_pick]['mousemove'](e, color_pick);
	}
}

function onMouseUp(e) {
	tool_handler[tool_pick]['mouseup'](e, color_pick);
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
