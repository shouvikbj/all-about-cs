// // ||VARIABLES|| \\
// // Using Var
// var age=20;
// var age=24;
// var age=30;
// console.log(age);
// let name="Anasmita Math";
// // Using Let
// // let name="Smita"; It gives error 
// console.log(name);
// name="Pupu"; // Update
// console.log(name);
// // Using Const
// const pi=3.14;
// // pi=4.5; //Runtime Error
// console.log(pi);
// // Mixed Value
// const num1 = 23;
// const num2=34;
// let total = num1 + num2;
// console.log(total);
// let sub = num1 - num2;
// console.log(sub);

// // ||DATATYPES|| \\
// /////////////////// Primitive Datatypes (7) ///////////////////
// /*Number*/
// let age=21;
// console.log(age);
// console.log(`The type of age is: ${typeof age}`);
// /*String*/
// let hobby="singing";
// console.log(hobby);
// console.log(`the type of hobby is: ${typeof hobby}`);
// /*Boolean*/
// let isEven=true;
// console.log(isEven);
// console.log(`The type of isEven is: ${typeof isEven}`);
// /*Undefined*/
// let x;
// console.log(x);
// console.log(`The type of x is: ${typeof x}`);
// /*Null*/
// let y=null;
// console.log(`The type of y is: ${typeof y}`);
// /*BigInt*/
// let z=BigInt("239005");
// console.log(z);
// console.log(`The type of y is: ${typeof z}`);
// /*Symbol*/
// let s=Symbol("Hello!");
// console.log(s);
// console.log(`The type of y is: ${typeof s}`);
// /////////////////// Non Primitive Datatype ////////////////////
// /*Objects*/
// const person={
//     name:"Anasmita Math",
//     age:20,
//     city:"Panskura",
//     details:{
//         mail:"smita225@gmail.com",
//         contact:['1238567894','9876543217']
//     }
// };
// console.log(person);
// console.log(typeof person);
// //console.log(person.name);
// console.log(person["name"]);
// console.log(person.city);
// console.log(person.details.mail);
// console.log(person.details.contact[1]);

// || Conditional Statements || \\
// Odd-Even
let x=35;
if(x%2==0)
    console.log("The number is Even");
else
    console.log("The number is Odd");
// Negative-Positive Number
let y=-24;
if(y>0)
    console.log("The number is Positive");
else if(y<0)
    console.log("The number is Negative");
else
    console.log("This is Zero");

