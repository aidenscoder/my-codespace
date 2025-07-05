import { createCanvas } from "canvas";

let screen = createCanvas(800,600);
let draw = screen.getContext('2d');

draw.fillStyle = 'blue';
draw.fillRect(400,300,50,50);