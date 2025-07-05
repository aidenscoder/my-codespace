"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var process_1 = require("process");
var readline_1 = require("readline");
var rl = (0, readline_1.createInterface)(process_1.stdin, process_1.stdout);
rl.question("whats your name:", function (answer) {
    console.log("hello,".concat(answer));
});
