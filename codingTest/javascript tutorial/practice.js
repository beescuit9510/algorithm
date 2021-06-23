// names[0]===names2[0] ? console.log("True"):console.log("False")

const people = [
  { name: "sharukh", age: 10, position: "bunny" },
  { name: "khan", age: 20, position: "cat" },
  { name: "afridi", age: 30, position: "elephant" },
  { name: "cuppy", age: 40, position: "monkey" },
];

console.log(window);
console.dir(document);

document.getElementById("h1").setAttribute("draggable", "true");

document.getElementById("h1").addEventListener("drag", function () {
  this.style.backgroundImage = "url(./images/paw_print.jpg)";
  this.style.color = "white";
});

let mainArr = [document.getElementsByTagName("main")];
mainArr.forEach(function (each, i) {
  each.item(i).setAttribute("id", "main");
});
let newNode = document.createElement("p");
newNode.innerHTML = "its time";
document.getElementById("main").appendChild(newNode);

function timeForWeb() {
  let time = new Date();
  return (newNode.innerHTML = time.toString());
}

window.setInterval(timeForWeb, 1000);

let counterFunc = (function () {
  let count = 0;
  return () => (count += 1);
})();

let newUl = document.createElement("ul");
document.getElementById("main").appendChild(newUl).setAttribute("id", "ul");

for (let i = 0; i < 10; i++) {
  let li = document
    .getElementById("ul")
    .appendChild(document.createElement("li"));
  li.appendChild(document.createTextNode("hello"));
}
[...document.getElementsByTagName("li")].forEach((each, i) =>
  each.setAttribute("id", "li")
);

document
  .querySelectorAll("li#li")
  .forEach((each) => (each.style.color = "red"));

let all_ul_children = [...document.querySelectorAll("#ul")];

let all_ul_grandchildren = all_ul_children.map((each) => each.children);

console.log(all_ul_children);
console.log(all_ul_children[0]);

let ul_chilren = [...document.querySelectorAll("#ul")[0].children];

ul_chilren.forEach((each) => (each.style.color = "blue"));

console.log(counterFunc.length);

document.getElementById("ul").previousElementSibling.style.color = "red";

let newPara = document.createElement("p");
newPara.innerHTML = "hello im new node";
let target_node = document.getElementById("h1");
target_node.parentNode.insertBefore(newPara, target_node.nextSibling);

console.log(document.getElementById("h1").getAttributeNames());
console.log(document.getElementById("h1").getAttributeNS("id", "draggable"));

let target = document.getElementById("ul");
let new_element = document.createElement("p");
let new_text = document.createTextNode("new text");
new_element.appendChild(new_text);
new_element.classList.add("new_element");
// target.replaceWith(new_element);

// let target_main = [...document.getElementsByClassName("new_element")][0]
// .parentElement;

// target_main.replaceChild(target, target_main.children[0]);

let new_li = document.createElement("li");
new_li.appendChild(document.createTextNode("new li"));

let target2 = document.getElementById("ul");
target.prepend(new_li);

console.log(document.getElementById("ul").innerHTML);
console.log(document.getElementById("ul").innerText);

let new_ul = document.createElement("ul");
new_ul.innerHTML = document.getElementById("ul").innerHTML;
document.getElementById("main").appendChild(new_ul);
new_ul.childNodes.forEach((each) => (each.innerText = "hi"));

console.log(document.body.style);

let new_btn = document.createElement("button");
target = document.getElementById("main");
new_btn.innerText = "click!";
new_btn.style.width = "70px";
new_btn.style.height = "30px";
new_btn.style.border = "5px solid black";
new_btn.classList.add("hello");
new_btn.classList.add("cherry");
new_btn.classList.add("bttn");
target.insertBefore(new_btn, target.childNodes[target.childNodes.length]);

new_btn.addEventListener("click", () => {
  new_btn.classList.forEach((each) => {
    each == "bttn" ? new_btn.classList.remove(each) : null;
  });
  return alert(new_btn.classList);
});

new_btn.addEventListener("click", () => {
  new_btn.classList.contains("bttn") ? new_btn.classList.remove("bttn") : null;
  return alert(new_btn.classList);
});

let h1_sibling = document.getElementById("h1").nextSibling;
let new_input = document.createElement("INPUT");
new_input.setAttribute("type", "text");
h1_sibling.parentElement.insertBefore(new_input, h1_sibling);
// new_input.addEventListener('keydown',()=>alert('hello'));'/////////////////pooooooooooo
new_input.addEventListener(
  "keydown",
  (event) => (event.currentTarget.style.color = "red")
);

new_input.addEventListener("keydown", (event) => alert(event.type));

let element_ul_children = [...document.getElementById("ul").children];

let click = document.getElementById("main").lastChild;
click.setAttribute("id", "click");

for (let i = 0; i < 30; i++) {
  click.parentElement.insertBefore(document.createElement("br"), click);
}
element_ul_children.forEach((each) => {
  each.addEventListener(
    "click",
    (event) => (event.currentTarget.style.color = "red")
  );
});

element_ul_children.forEach((each) => {
  each.replaceChild(document.createElement("a"), each.firstChild);
  each.firstChild.setAttribute("href", "#click");
  each.firstChild.appendChild(document.createTextNode("hello"));
});

// element_ul_children.forEach((each)=>{each.addEventListener("click", (event) => event.preventDefault());})

let h1 = document.getElementById("h1");
let text_node = document.createTextNode("hello");
let child = document.createElement("p");
child.appendChild(text_node);
h1.appendChild(child);

// Difference between target / currentTarget
h1.addEventListener(
  "click",
  (event) => (event.currentTarget.style.color = "red")
);
h1.addEventListener("click", (event) => (event.target.style.color = "red"));

let ul = document.getElementById("ul");
ul.addEventListener("click", (event) => event.preventDefault());

// ul.addEventListener("click", (event) => {event.stopPropagation();});

// ul.addEventListener('click',(event)=>{event.target.hasAttribute("href")
// ? event.target.style.backgroundColor = "yellow":null;})

// ul.addEventListener('click', (event)=>{event.currentTarget.style.backgroundColor = "red"; event.stopPropagation()})

let clone_btn = new_btn.cloneNode();
let clone_text = document.createTextNode(new_btn.textContent);
clone_btn.appendChild(clone_text);
new_btn.replaceWith(clone_btn);

new_btn.style.color = "red";

let form = [...document.getElementsByTagName("form")];
let main = document.getElementById("main");
main.insertBefore(form[0], main.lastChild);

form[0].addEventListener("submit", (e) => {
  e.preventDefault();
  alert(form[0].lastElementChild.previousElementSibling.value);
});

localStorage.setItem("name", "sharukh");
localStorage.setItem("name", "sharukh");
localStorage.setItem("name", "sharukh");

localStorage.clear();

function isArray(myArray) {
  return myArray.constructor.toString().indexOf('Array')
}

console.log(isArray(people));


let json_people = JSON.stringify(people)
// localStorage.setItem('people', json_people)
localStorage.clear()

let check_localSorage = localStorage.getItem('people')
check_localSorage=[] ? console.log('No values'):console.log(JSON.parse(check_localSorage))






pow.List = {};
function pow(a,b){
  if(pow.List[`${a}^${b}`]){
    console.log('exist')
  } else{
    let r = a;
    for(let i=0; i<b; i++){
      r *= b;}
    pow.List[`${a}^${b}`] = r
    console.log(pow.List)
  }}


pow(2,2)
pow(2,4)
pow(3,7)
pow(3, 7);



function pow2(x,y){
  // y==undefined ? y=2:null;
  y = typeof y=="undefined" ? 2:y;
  let r = 1;
  for(let i=0; i<y;i++){
    r *= x;
  }
  console.log(r)
}

pow2(2);
pow2(5,3);
pow2(3);
pow2(4);


function pow3(x,y, ...extra){
  pow3.extras = [];
  let r = 1;
  for(let i=0; i<y;i++){
    r *= x;
  }
  pow3.extras.push(r)
  r =1;
  for(let i=0; i<extra.length;i++){
    if (i%2==0 && extra[i+1]){
      for (let j=0; j<extra[i+1]; j++)
        r *= extra[i]
        pow3.extras.push(r)
      r = 1;}
    }
  console.log(pow3.extras)
}

pow3(2, 3)
pow3(2, 2);
pow3(3, 2);
pow3(4, 2);
pow3(5, 2, 2,2, 5,2,6,2,6);



function pow4(x, y, ...extra){
  pow4.extras = [];
  function inner(x, y){
    let r = 1;
    for(let i=0; i<y;i++){
     r *= x;
    }
    pow4.extras.push(r)
    extra.shift(); extra.shift();
  }
  inner(x,y)
  if(extra[0]&&extra[1]){
    inner(extra[0],extras[1])
  }
  console.log(pow4.extras)
}

pow3(2, 3);
pow3(2, 2);
pow3(3, 2);
pow3(4, 2);
pow3(5, 2, 2, 2, 5, 2, 6, 2, 6);



function pow5(a,b){
  if([a,b].every(e=>typeof e!==typeof 1)){
    throw "Not an invaild inputs, check again"
  } else{
    console.log(Math.pow(a,b))
  }
}

pow5(1,2)
pow5(2,2);
// pow5('2','2')


let user = {
  active:true
}

let teacher = {
  teaching:["math","science"]
}
Object.setPrototypeOf(teacher, user)
console.log(teacher)

function Person(name,age,position){
  this.name=name;
  this.age = age;
  this.position=position;

}

Person.prototype.sayHello = function(){return this.name+" says hello"}

let sharukh = new Person('sharukh',23,'cuppy')
sharukh.company = 'python'
console.log(sharukh)
console.log(Object.getPrototypeOf(sharukh))
console.log(Object.getOwnPropertyNames(sharukh))
console.log(sharukh.sayHello())




function Friend(name, age, position){
  this.name = name
  this.age = age
  this.position = position
}

Friend.prototype = new User()
User.prototype.sayHi = function(){return `${this.name} says Hi`}

let sharukh_clone = new Friend('sharukh',24,'cuppy')

console.log(sharukh_clone.sayHi());
console.log(Object.getPrototypeOf(sharukh_clone))
console.log(sharukh_clone)

//hasOwnProperty dose not check prototype 
console.log(sharukh_clone.hasOwnProperty("sayHi"));
console.log('sayHi' in sharukh_clone)


// console.log(Object.getOwnPropertyNames(sharukh_clone))
// console.log(Object.getOwnPropertyNames(Object.getPrototypeOf(sharukh_clone)))

let propertyListOfsharukh = [];
for(let prop in sharukh_clone){
  propertyListOfsharukh.push(prop)
}
// console.log(propertyListOfsharukh)



function User(){
  this.active = true;
}

console.log(sharukh_clone)


let literalString = "This is a literal string";
let stringObject = new String("String created with constructor");
console.log(typeof literalString)
console.log(typeof stringObject)
console.log(literalString instanceof String)
console.log(String instanceof Object)
console.log('hello' instanceof String)



let funcA = function(){
  let x = 0
  function inner(){
    x++;
    return(x)
  }
  return inner
}();

console.log()
console.log(funcA())
console.log(funcA());



let counterFunc = (function () {
  let count = 0;
  return () => (count += 1);
})();

counterFunc();
counterFunc();
console.log(counterFunc());