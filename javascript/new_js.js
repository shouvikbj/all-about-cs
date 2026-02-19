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

// // || Conditional Statements || \\
// // Odd-Even
// let x=35;
// if(x%2==0)
//     console.log("The number is Even");
// else
//     console.log("The number is Odd");
// // Negative-Positive Number
// let y=-24;
// if(y>0)
//     console.log("The number is Positive");
// else if(y<0)
//     console.log("The number is Negative");
// else
//     console.log("This is Zero");

// // || Arrays || \\
// let arr=["Apple","Mango","Grapes",(12,23,45),{Marks:89}];
// console.log(arr);
// console.log(arr.length);
// console.log(arr[2]);
// console.log(arr[5]);
// arr[0]="orange";
// console.log(arr);
// for(let i=0;i<arr.length;i++)
//     console.log(arr[i]);
// let cities=["Kolkata","Delhi","Bangalore","Pune"];
// for(let city of cities){
//     console.log(city);
//     console.log(city.toUpperCase());
// }
// //Array Methods
// cities.push("Chennai");
// console.log(cities);
// cities.pop();
// console.log(cities);
// cities.unshift("Haldia");
// console.log(cities);
// //Join multiple arrays
// let fru1=["Watermelon","Banana","Pear"];
// let fru2=["Strawberry","Cherry","Lychee"];
// let Fruit=fru1.concat(fru2);
// console.log(Fruit);

// // || Loops || \\
// let cities=["Kolkata","Delhi","Bangalore","Pune"];
// for(let i=0;i<cities.length;i++)
// {
//     console.log(`${JSON.stringify(cities[i])} is at index ${i}`);
// }
// const person={
//     name:"Anasmita Math",
//     age:20
// }
// console.log(person);
// console.log(JSON.stringify(person));
// while (cities.length > 0) {
//     const city = cities.pop();
//     console.log(`Removed ${JSON.stringify(city)} from the array. Remaining cities: ${JSON.stringify(cities)}`);
// }
// || Functions || \\
function func(user_name) {
   console.log(`Hello, ${user_name}!`);
}
func("Anasmita");
func("Math");
func("Student");
const checkAge = (age) => {
    if (age < 18) {
        return "You are a minor.";
    } 
    else if (age >= 18 && age < 60) {
        return "You are an adult.";
    } else {
        return "You are a senior citizen.";
    }
}
console.log(checkAge(20)); 
console.log(checkAge(12));
console.log(checkAge(75));