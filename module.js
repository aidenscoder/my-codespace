import { createInterface } from "readline";


const rl = createInterface({
  input: process.stdin,
  output: process.stdout
});

export const input = (message) => {
    rl.question(message,(answer) => {
      rl.close();
      return answer;
    });
};
