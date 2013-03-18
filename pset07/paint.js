
var WIDTH = 600;
var HEIGHT = 400;

var COLORS = {
  red: "#f00",
  orange: "#f60",
  yellow: "#ff0",
  green: "#0f0",
  blue: "#00f",
  indigo: "#509",
  violet: "#909",
  black: "#000"
};


// Globals for this file
var canvas;
var ctx;


function init() {
  document.onselectstart = function(){ return false; };
  canvas = document.getElementById("paint");
  canvas.width = WIDTH;
  canvas.height = HEIGHT;
  ctx = canvas.getContext('2d');
}

window.addEventListener("load", init, false);
