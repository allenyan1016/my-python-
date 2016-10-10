'use strict'
/*
function abs(x,y) {
	if (x>y){
		return x;
	}else{
		return y;
	}
}

alert(abs(1,5));

var mine = {};
mine.name = 'abs';
mine.verson = 1.0;
mine.abs = function(x,y){
	if (x>y){
		return x;
	}else{
		return y;
	}
}

alert(mine.abs(1,6))

mine.test = function(){
	return 1;
}

alert(mine.test())
*/
//定义一个对象xiaoming，在对象的方法属性中先捕获this，再在子方法中使用已经捕获到的this
var xiaoming = {
	name : 'xiaoming',
	birth : 1993,
	age:function(){
		var that = this;
		function getAge(){
			var y = new Date().getFullYear();
			return y-that.birth;
		}
		return getAge();
	} 
};

//window.alert(xiaoming.age())
console.log(xiaoming.age());

var date1 = new Date();
//window.alert(date1.getMonth());
console.log(date1.getMonth());

var m = '010-4654564';
var r = /^\d{3}\-\d{3,8}$/;
//alert(r.test(m));
console.log(r.test(m));

var xiaoming2 = {
	name : 'xiaoming',
	age : 16,
	school : 'middle-school',
	add : 'beijing',
	grade : 64,
	toJSON: function(){
		return {
			'name':this.name,
			'age':this.age
		}
	}
};

//定义一个函数，可以将对象或者JSON格式的数据的值转换成大写
function valueChange(key,value){
	if (typeof value === "string"){
		return value.toUpperCase();
	}
	return value;
}
console.log(JSON.stringify(xiaoming2));
console.log(JSON.stringify(xiaoming2,['name','age']));
console.log(JSON.stringify(xiaoming2,valueChange));

//定义一个xiaoming3对象，最初想定义成JSON格式数据
var xiaoming3 = {
	"name" : 'xiaoming',
	"age" : 16,
	"school" : 'W3C',
	"grade" : 'A'
};

//将对象转换成JSON格式之后查看转后的数据类型
console.log(typeof JSON.stringify(xiaoming3));

//定义一个原型对象
var Student = {
	name : 'xxx',
	age : 20,
	//定义一个方法属性
	skill : function(){
		console.log(this.name + " is running...");
	}
}

//定义一个方法可以创建对象
function createStudent(name){
	//初始化对象
	var s = Object.create(Student);
	//初始化对象的name属性
	s.name = name;
	return s;
}

//创建一个haha对象
var haha = createStudent("haha");

console.log(haha.name);
//无法正确输出haha的类型
console.log(typeof haha);
console.log(haha.skill());

//比较haha对象是否指向原型对象
console.log(haha.__proto__ === Student);

function add(name){
	this.name = name;
	this.age = 120;
}

var q = new add('erha');
console.log(q.name);
console.log(q.age);