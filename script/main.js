//Setting the main variables and constants
const canvas = document.getElementById("gameCanvas");
const context = canvas.getContext('2d');
const debug = document.getElementById("debug");

let windowHeight = window.innerHeight;
let windowWidth = window.innerWidth;
let d;
d = (windowWidth <= windowHeight/2) ? windowWidth : windowHeight/2;
let c = d/2, t = d/4, h = Math.sqrt((d/2)*(d/2) - (d/4)*(d/4));

canvas.height = h*2;
canvas.width = d;
debug.innerText = "canvas side = " + d;

//Test, drawing a line :
context.moveTo(c, h);
context.lineTo(c, 0);
context.stroke();

//Test, drawing a polygon in blue :
context.beginPath();
context.moveTo(10,10);
context.lineTo(40, 40);
context.lineTo(100, 40);
context.lineTo(70, 10);
context.lineTo(10, 10);
context.fill();