//tsc main.ts & main.js
import {input} from "../my-codespace/module";

let name = input("your name:",
    (answer:string) => {
        console.log(`Hello, ${answer}`);
    }
);