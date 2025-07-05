"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var canvas_1 = require("canvas");
var screen = (0, canvas_1.createCanvas)(800, 600);
var draw = screen.getContext('2d');
draw.fillStyle = 'blue';
draw.fillRect(400, 300, 50, 50);
