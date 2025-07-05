import { stdin, stdout } from "process";
import { createInterface } from "readline";

const rl = createInterface(stdin,stdout);

rl.question("whats your name:",
    (answer) => {
        console.log(`hello,${answer}`);
    }
);

console.log("jkw");