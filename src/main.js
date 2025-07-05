"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
var ConstructorError = /** @class */ (function (_super) {
    __extends(ConstructorError, _super);
    function ConstructorError(message) {
        var _this = this;
        throw _this = _super.call(this, message) || this;
        return _this;
    }
    return ConstructorError;
}(Error));
var Expressions = /** @class */ (function () {
    function Expressions() {
        throw new ConstructorError("Cannot a make instance of this class");
    }
    Expressions.If = function (condition) {
        return function (to_exec) {
            if (condition) {
                to_exec();
            }
        };
    };
    Expressions.While = function (condition) {
        return function (to_exec) {
            while (condition()) {
                to_exec();
            }
        };
    };
    Expressions.Inside = function (iterable) {
        return function (to_exec) {
            for (var _i = 0, iterable_1 = iterable; _i < iterable_1.length; _i++) {
                var items = iterable_1[_i];
                to_exec(items);
            }
        };
    };
    Expressions.WriteFile = function (file_name) {
        return function (content) {
            fs.writeFileSync(file_name, content, "utf-8");
        };
    };
    Expressions.ReadFile = function (file_name) {
        return fs.readFileSync(file_name, "utf-8");
    };
    return Expressions;
}());
console.log("".concat(Expressions.ReadFile("README.md")));
