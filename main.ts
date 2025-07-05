import { Engine, World, Bodies } from "matter-js";

// Create engine
const engine = Engine.create();

// Create bodies
const box = Bodies.rectangle(400, 200, 80, 80);
const ground = Bodies.rectangle(400, 610, 810, 60, { isStatic: true });

// Add bodies to the world
World.add(engine.world, [box, ground]);

// Run the engine manually in a loop
setInterval(() => {
  Engine.update(engine, 1000 / 60);
  console.log(`Box position: x=${box.position.x.toFixed(2)}, y=${box.position.y.toFixed(2)}`);
}, 1000 / 60);

