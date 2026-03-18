# JavaScript Warm Up — Learning Objectives

## 1. Why JavaScript Programming is Amazing

JavaScript is one of the most powerful and versatile programming languages in the world:

- **Runs everywhere** — in browsers, on servers (Node.js), mobile apps, desktop apps
- **Only language native to browsers** — essential for web interactivity
- **Huge ecosystem** — npm has millions of packages
- **Asynchronous by nature** — handles real-time data, APIs, events efficiently
- **Full-stack capable** — frontend AND backend with the same language
- **Massive community** — most popular language on GitHub for years

---

## 2. How to Run a JavaScript Script

### In the browser
Open DevTools (F12) → Console tab → type your code directly.

### With Node.js (terminal)
```bash
node my_script.js
```

### With a shebang (executable script)
```javascript
#!/usr/bin/node
console.log("Hello, World!");
```
```bash
chmod +x my_script.js
./my_script.js
```

---

## 3. How to Create Variables and Constants

```javascript
// Variable (can change)
let age = 25;
age = 26; // ✅ allowed

// Constant (cannot change)
const name = "Techium";
name = "Other"; // ❌ TypeError

// Old way (avoid)
var city = "Paris";
```

---

## 4. Differences Between `var`, `const` and `let`

| | `var` | `let` | `const` |
|---|---|---|---|
| **Scope** | Function | Block `{}` | Block `{}` |
| **Reassignable** | ✅ | ✅ | ❌ |
| **Hoisted** | ✅ (undefined) | ✅ (not initialized) | ✅ (not initialized) |
| **Re-declarable** | ✅ | ❌ | ❌ |
| **Use** | ❌ Avoid | ✅ Use | ✅ Use |

```javascript
// var — function scoped, avoid it
var x = 1;
if (true) {
    var x = 2; // same variable!
    console.log(x); // 2
}
console.log(x); // 2 ← leaks out of block!

// let — block scoped
let y = 1;
if (true) {
    let y = 2; // different variable
    console.log(y); // 2
}
console.log(y); // 1 ← unchanged

// const — block scoped, cannot be reassigned
const PI = 3.14;
// PI = 3; // ❌ TypeError
```

> **Best practice:** Use `const` by default. Use `let` when you need to reassign. Never use `var`.

---

## 5. All Data Types Available in JavaScript

### Primitive types
```javascript
// String
let name = "Holberton";
let greeting = `Hello, ${name}!`; // template literal

// Number
let age = 25;
let price = 9.99;

// Boolean
let isAdmin = true;
let isLoggedIn = false;

// undefined — declared but not assigned
let x;
console.log(x); // undefined

// null — intentionally empty
let user = null;

// BigInt — very large integers
let bigNumber = 9007199254740991n;

// Symbol — unique identifier
let id = Symbol("id");
```

### Non-primitive type
```javascript
// Object
let person = { name: "Alice", age: 30 };

// Array (special object)
let colors = ["red", "green", "blue"];

// Function (special object)
let greet = function() { return "Hello!"; };
```

### Check a type
```javascript
typeof "hello"      // "string"
typeof 42           // "number"
typeof true         // "boolean"
typeof undefined    // "undefined"
typeof null         // "object" ← known JS quirk
typeof {}           // "object"
typeof []           // "object"
typeof function(){} // "function"
```

---

## 6. How to Use `if` / `if...else` Statements

```javascript
let score = 85;

// Simple if
if (score >= 90) {
    console.log("Excellent!");
}

// if...else
if (score >= 90) {
    console.log("Excellent!");
} else {
    console.log("Keep working!");
}

// if...else if...else
if (score >= 90) {
    console.log("A");
} else if (score >= 80) {
    console.log("B");
} else if (score >= 70) {
    console.log("C");
} else {
    console.log("F");
}

// Ternary operator (shorthand)
let result = score >= 90 ? "Pass" : "Fail";
```

---

## 7. How to Use Comments

```javascript
// Single-line comment

/*
  Multi-line comment
  Used for longer explanations
*/

/**
 * JSDoc comment — used to document functions
 * @param {string} name - The user's name
 * @returns {string} A greeting message
 */
function greet(name) {
    return `Hello, ${name}!`;
}
```

---

## 8. How to Assign Values to Variables

```javascript
// Simple assignment
let x = 10;
let name = "Alice";
let isActive = true;

// Multiple assignment
let a, b, c;
a = b = c = 0;

// Destructuring assignment
let [first, second] = [1, 2];
let { city, country } = { city: "Paris", country: "France" };

// Compound assignment operators
let n = 10;
n += 5;  // n = n + 5  → 15
n -= 3;  // n = n - 3  → 12
n *= 2;  // n = n * 2  → 24
n /= 4;  // n = n / 4  → 6
n %= 4;  // n = n % 4  → 2
n **= 3; // n = n ** 3 → 8
```

---

## 9. How to Use `while` and `for` Loops

### `while` loop
```javascript
let i = 0;
while (i < 5) {
    console.log(i); // 0, 1, 2, 3, 4
    i++;
}
```

### `do...while` loop (executes at least once)
```javascript
let i = 0;
do {
    console.log(i);
    i++;
} while (i < 5);
```

### `for` loop
```javascript
for (let i = 0; i < 5; i++) {
    console.log(i); // 0, 1, 2, 3, 4
}
```

### `for...of` loop (arrays)
```javascript
let colors = ["red", "green", "blue"];
for (let color of colors) {
    console.log(color);
}
```

### `for...in` loop (objects)
```javascript
let person = { name: "Alice", age: 30 };
for (let key in person) {
    console.log(key, person[key]);
    // name Alice
    // age 30
}
```

---

## 10. How to Use `break` and `continue`

### `break` — exits the loop immediately
```javascript
for (let i = 0; i < 10; i++) {
    if (i === 5) break; // stops at 5
    console.log(i); // 0, 1, 2, 3, 4
}
```

### `continue` — skips the current iteration
```javascript
for (let i = 0; i < 10; i++) {
    if (i % 2 === 0) continue; // skips even numbers
    console.log(i); // 1, 3, 5, 7, 9
}
```

---

## 11. What is a Function and How to Use It

A function is a reusable block of code that performs a specific task.

```javascript
// Function declaration
function add(a, b) {
    return a + b;
}

// Function expression
const multiply = function(a, b) {
    return a * b;
};

// Arrow function
const divide = (a, b) => a / b;

// With default parameters
function greet(name = "World") {
    return `Hello, ${name}!`;
}

// Call a function
console.log(add(3, 4));       // 7
console.log(multiply(3, 4));  // 12
console.log(divide(10, 2));   // 5
console.log(greet());         // Hello, World!
console.log(greet("Alice"));  // Hello, Alice!
```

---

## 12. What a Function Without `return` Returns

A function that has no `return` statement returns `undefined`.

```javascript
function sayHello() {
    console.log("Hello!");
    // no return statement
}

let result = sayHello(); // prints "Hello!"
console.log(result);     // undefined

function empty() {
    return; // explicit empty return
}
console.log(empty()); // undefined
```

---

## 13. Scope of Variables

Scope determines where a variable is accessible.

```javascript
// Global scope — accessible everywhere
let globalVar = "I'm global";

function myFunction() {
    // Function scope
    let localVar = "I'm local";
    console.log(globalVar); // ✅ accessible
    console.log(localVar);  // ✅ accessible
}

console.log(globalVar); // ✅ accessible
console.log(localVar);  // ❌ ReferenceError

// Block scope (let and const only)
if (true) {
    let blockVar = "I'm block scoped";
    const blockConst = "Me too";
    console.log(blockVar); // ✅
}
console.log(blockVar); // ❌ ReferenceError

// Closure — function remembers its outer scope
function counter() {
    let count = 0;
    return function() {
        count++;
        return count;
    };
}
const increment = counter();
console.log(increment()); // 1
console.log(increment()); // 2
```

---

## 14. Arithmetic Operators

```javascript
let a = 10;
let b = 3;

console.log(a + b);  // 13   — Addition
console.log(a - b);  // 7    — Subtraction
console.log(a * b);  // 30   — Multiplication
console.log(a / b);  // 3.33 — Division
console.log(a % b);  // 1    — Modulo (remainder)
console.log(a ** b); // 1000 — Exponentiation

// Increment / Decrement
let x = 5;
x++;    // x = 6 (post-increment)
++x;    // x = 7 (pre-increment)
x--;    // x = 6 (post-decrement)
--x;    // x = 5 (pre-decrement)

// Math object
Math.abs(-5);       // 5
Math.round(4.7);    // 5
Math.floor(4.9);    // 4
Math.ceil(4.1);     // 5
Math.max(1, 2, 3);  // 3
Math.min(1, 2, 3);  // 1
Math.sqrt(16);      // 4
Math.random();      // random float between 0 and 1
```

---

## 15. How to Manipulate a Dictionary (Object)

In JavaScript, dictionaries are called **Objects**.

```javascript
// Create an object
let person = {
    name: "Alice",
    age: 30,
    city: "Paris"
};

// Access values
console.log(person.name);    // "Alice" — dot notation
console.log(person["age"]);  // 30 — bracket notation

// Add a property
person.email = "alice@example.com";

// Modify a property
person.age = 31;

// Delete a property
delete person.city;

// Check if a key exists
console.log("name" in person);              // true
console.log(person.hasOwnProperty("city")); // false

// Loop through an object
for (let key in person) {
    console.log(`${key}: ${person[key]}`);
}

// Get all keys / values / entries
Object.keys(person);    // ["name", "age", "email"]
Object.values(person);  // ["Alice", 31, "alice@example.com"]
Object.entries(person); // [["name", "Alice"], ["age", 31], ...]

// Merge objects
let extra = { job: "Developer" };
let merged = { ...person, ...extra };
```

---

## 16. How to Import a File

### CommonJS (Node.js — default)

**Export:**
```javascript
// math.js
function add(a, b) { return a + b; }
function multiply(a, b) { return a * b; }

module.exports = { add, multiply };
```

**Import:**
```javascript
// main.js
const { add, multiply } = require('./math');
console.log(add(2, 3));      // 5
console.log(multiply(2, 3)); // 6

// Import entire module
const math = require('./math');
console.log(math.add(2, 3));
```

### ES Modules (modern JS)

**Export:**
```javascript
// math.js
export function add(a, b) { return a + b; }
export const PI = 3.14;
export default function multiply(a, b) { return a * b; }
```

**Import:**
```javascript
// main.js
import multiply, { add, PI } from './math.js';
console.log(add(2, 3));      // 5
console.log(multiply(2, 3)); // 6
console.log(PI);             // 3.14

// Import everything
import * as math from './math.js';
console.log(math.add(2, 3));
```
