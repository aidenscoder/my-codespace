import * as fs from "fs";

class ConstructorError extends Error {
    constructor(message: string) {
        throw super(message);
        this.name = 'ConstructorError';
    }
}

class Expressions {

    constructor() {
        throw new ConstructorError("Cannot a make instance of this class");
    }

    static If(condition: boolean) {
        return function (to_exec:() => void) {
            if (condition) { to_exec() }
        }
    }

    static While(condition: () => boolean) {
        return function (to_exec: () => void) {
            while (condition()) { to_exec() }
        };
    }

    static Inside(iterable: any) {
        return function (to_exec: (unpacked: any) => void) {
            for (const items of iterable) {
                to_exec(items);
            }
        };
    }

    static WriteFile(file_name:string){
        return function(content:string){
            fs.writeFileSync(file_name,content,"utf-8");
        }
    }

    static ReadFile(file_name:string){
        return fs.readFileSync(file_name,"utf-8");
    }
}


