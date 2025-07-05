import { createInterface } from "readline";

export const input = (message,script) => {
    const rl = createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question(message,(answer) => {
      if (answer != ""){
        script(answer);
        rl.close();
      }
      rl.close();
    });
};