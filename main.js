"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var matter_js_1 = require("matter-js");
// Create engine
var engine = matter_js_1.Engine.create();
// Create bodies
var box = matter_js_1.Bodies.rectangle(400, 200, 80, 80);
var ground = matter_js_1.Bodies.rectangle(400, 610, 810, 60, { isStatic: true });
// Add bodies to the world
matter_js_1.World.add(engine.world, [box, ground]);
// Run the engine manually in a loop
setInterval(function () {
    matter_js_1.Engine.update(engine, 1000 / 60);
    console.log("Box position: x=".concat(box.position.x.toFixed(2), ", y=").concat(box.position.y.toFixed(2)));
}, 1000 / 60);
