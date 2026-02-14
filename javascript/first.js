// client side scripting language
// used to make web pages interactive
// runs in the browser
// can be used on the server side with Node.js

// variables
// const my_name = "Shouvik";
// // my_name = "Shouvik Bajpayee"; // error: cannot reassign a constant variable
// console.log(my_name);

// let my_age = 25;
// console.log(my_age);
// my_age = 26; // can reassign a let variable
// console.log(my_age);

// console.log(my_city);

// var my_city = "Haldia";
// console.log(my_city);
// my_city = "Panskura"; // can reassign a var variable
// console.log(my_city);

// data types
// // string
// const my_name = "Shouvik";
// console.log(my_name);

// // number
// const age = 25;
// console.log(age);

// // boolean
// const is_student = true;
// console.log(is_student);

// // null
// const null_value = null;
// console.log(null_value);

// // undefined
// let undefined_value;
// console.log(undefined_value);

// object
// const person = {
//     name: "Shouvik",
//     age: 28,
//     city: "Haldia",
//     home: "Panskura",
//     address: {
//         village: "Bahargram",
//         post_office: "Panskura (R.S.)",
//         police_station: "Panskura",
//         pin: 721152,
//         contact: ['1234567890', '0987654321']
//     }
// };
// console.log(person);
// console.log(person.name);
// console.log(person.age);
// console.log(person.city);
// console.log(person.home);
// console.log(person.address);
// console.log(person.address.village);
// console.log(person.address.post_office);
// console.log(person.address.police_station);
// console.log(person.address.pin);
// console.log(person.address.contact);
// console.log(person.address.contact[0]);
// console.log(person.address.contact[1]);

// arrays
const fruits = ["apple", "banana", "orange", "grape", 0, true, null, undefined, { name: "fruit" }, [1, 2, 3]];
// console.log(fruits);
// console.log(fruits[0]);
// console.log(fruits[1]);
// console.log(fruits[2]);
// console.log(fruits[3]);
// console.log(fruits[4]);
// console.log(fruits[5]);
// console.log(fruits[6]);
// console.log(fruits[7]);
// console.log(fruits[8]);
// console.log(fruits[9]);
// fruits.push("mango"); // add an element to the end of the array
// console.log(fruits);
// fruits.pop(); // remove the last element of the array
// console.log(fruits);
// fruits.unshift("strawberry"); // add an element to the beginning of the array
// console.log(fruits);
// fruits.shift(); // remove the first element of the array
// console.log(fruits);
// console.log(fruits.length);
// const new_arr = ["Bajpayee", ...fruits, "Asst. Prof."] // spread operator to create a new array by combining existing arrays and adding new elements
// console.log(new_arr);

// conditionals
// const age = 28;
// if (age < 18) {
//     console.log("You are a minor.");
// } else if (age >= 18 && age < 60) {
//     console.log("You are an adult.");
// } else {
//     console.log("You are a senior citizen.");
// }

// loops
// for (let i = 0; i < 5; i++) {
//     console.log(i);
// }
// for (const fruit of fruits) {
//     // fruit = "hacked"; // reassigning the loop variable does not affect the original array
//     console.log(fruit);
// }
// for (let i = 0; i < fruits.length; i++) {
//     console.log(`${JSON.stringify(fruits[i])} is at index ${i}`);
// }

// const person = {
//     name: "Shouvik",
//     age: 28
// }
// console.log(JSON.stringify(person)); // convert a JavaScript object to a JSON string
// const str = '{"name":"fruit"}';
// const obj = JSON.parse(str); // convert a JSON string to a JavaScript object
// console.log(obj);

// while (fruits.length > 0) {
//     const fruit = fruits.pop(); // remove the last element of the array and return it
//     console.log(`Removed ${JSON.stringify(fruit)} from the array. Remaining fruits: ${JSON.stringify(fruits)}`);
// }
// console.log("Final array:", fruits);

// formatted string literals (template literals)
// const first_name = "Shouvik";
// const age = 28;
// console.log(`My first name is "${first_name}" and I am ${age} years old.`);

// functions
// function greet(user_name) {
//     console.log(`Hello, ${user_name}!`);
// }

// greet("Shouvik"); // call the function with an argument
// greet("Bajpayee");
// greet("Asst. Prof.");

// Arrow functions
// ((user_name) => {
//     console.log(`Hello, ${user_name}!`);
// })("Shouvik"); // call the arrow function with an argument

// most commonly used arrow function syntax
// const greet = (user_name) => {
//     console.log(`Hello, ${user_name}!`);
// }

// greet("Shouvik"); // call the arrow function with an argument
// greet("Bajpayee");
// greet("Asst. Prof.");

// const checkAge = (age) => {
//     if (age < 18) {
//         return "You are a minor.";
//     } else if (age >= 18 && age < 60) {
//         return "You are an adult.";
//     } else {
//         return "You are a senior citizen.";
//     }
// }

// console.log(checkAge(28)); // call the arrow function with an argument
// console.log(checkAge(15));
// console.log(checkAge(65));