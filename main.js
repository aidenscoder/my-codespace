class point {
    constructor(x,y) {
        this.x = x;
        this.y = y;
    }

    print_points() {
        return [this.x, this.y];
    }
}

let my_point = point(1,2);
console.log(`${my_point.print_points()}`);