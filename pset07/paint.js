var WIDTH = 600;
var HEIGHT = 400;
var canvas;
var ctx;
var div_colors = document.getElementsByClassName("color");
var div_tools = document.getElementsByClassName("tool");
var div_sizes = document.getElementsByClassName("size");
var color_pick = "black"; //default tool color, can change.
var tool_pick = "pen"; //default tool is pen
var size_pick = "small"; //default tool size is small, or 3px
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

var SIZES ={
	"small": 3, "medium": 6, "large": 12
};

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
	makeSizeIcons()
  for (var color in COLORS) {
		div_colors[color].addEventListener("click", toolBarColors);
		div_colors[color].className += " no_highlight";
	}
	for (var tool in TOOLS) {
		div_tools[tool].addEventListener("click", toolBarTools);
		div_tools[tool].className += " no_highlight";
	}
	partialToolBarSize = _.partial(toolBarSize, 5);
	for (var size in SIZES) {
		div_sizes[size].addEventListener("click", partialToolBarSize);
		
		div_sizes[size].className += " no_highlight";
	}
	clearHighlights(div_colors['black']);
	div_colors['black'].className += " highlight";
	clearHighlights(div_tools['pen']);
	div_tools['pen'].className += " highlight";
	clearHighlights(div_sizes['small']);
	div_sizes['small'].className += " highlight";
	canvas.addEventListener('mousedown', onMouseDown);
	canvas.addEventListener('mouseup', onMouseUp);
	canvas.addEventListener('mousemove', onMouseMove);
	canvas.addEventListener('mouseout', onMouseOut);
}

//This generates the tool size icons for the toolbar.
function makeSizeIcons() {
	icon_list = {"small": document.getElementById("small_icon"), "medium": document.getElementById("medium_icon"), "large": document.getElementById("large_icon")};
	for (icon in icon_list){
	icon_list[icon].width = 32;
	icon_list[icon].height = 32;
	icon_list[icon].getContext('2d').arc(16, 16, SIZES[icon]/2, 0, 2 * Math.PI, false);
	icon_list[icon].getContext('2d').fillStyle = color_pick;
	icon_list[icon].getContext('2d').fill();
	}
}

//The function below handles an error where clicking size icons selected the canvas element rather than selecting the toolbar button.

//Below are helper functions for the event listening scripts below.
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

//Below is a helper function for clearing existing toolbar element highlights.

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

function toolBarSizes(e) {
	for (var size in SIZES) {
		clearHighlights(div_sizes[size]);
		div_sizes[size].className += " no_highlight";}
	clearHighlights(e.target);
	e.target.className += " highlight";
	size_pick = e.target.id;
	console.log("Tool size is now " + size_pick);
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
	//ctx.arc(16, 16, SIZES[size_pick]/2, 0, 2 * Math.PI, false);
	//ctx.fillStyle = color_pick;
	//ctx.fill();
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
