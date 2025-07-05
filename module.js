import { createInterface } from "readline";

export const input = (message) => {
    const rl = createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    rl.question(message,(answer) => {
      rl.close();
      return answer;
    });
};
