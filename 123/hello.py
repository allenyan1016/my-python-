# -*- coding: utf-8 -*-
"""
#打印python中的第一个程序
print ('hello world');
#定义一个等差数列，第一个数为1，差为3，等差数列个数为100个，求这个等差数列的和
i = 1
d = 3
n = 100
x100 = i + d*(n-1)
sum = (i+x100)*(n/2)
print (sum);
#
print (u'''静夜思

床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。''');
#
print (r'''
'nishuo' shenme 
nishisge "sahbi"
woshinidie''');
#输出字符串，使用反斜杠输出一些符号
s = 'python is very good \n I love "python"'
s1 = 'python is very good \n I love \"python\"'
print (s);
print (s1);

print (2.5 + 10 / 4);
"""
s = "nizaishuoshenme"

print (s) 		#输出这个整个的字符串
print (s[1:5])	#输出这个字符串的从下标1到5的字符串
print (s[10])	#输出这个字符串的第10个下标的字符串
print (s[2:])	#输出这个字符串的从第2个下标之后的所有的字符串

a = 21
b = 10
c = 0
if(a==b):
	print ('a=b')
else:
	print ('abudengyub')

a1 = 4
b1 = 5
if(a1==b1):
	print ('a1=b1')
else:
	print ('a1 != b1')

#输出1-10中的所有奇数
i = 1
while(i):
	if(i%2!=0):
		print (i)
	i=i+1
	if(i>10):
		break

c = 1
if c == 1:
	print ("c=1")
elif c == 2:
	print ("c=2")
elif c == 3:
	print ("c=3")

for letter in 'nishuoshenme':
	print ("当前字母是:",letter)

fruits = ['pingguo','xiangjiao','huluobo','bailuobo','huanggua','liulian']
for i in fruits:
	print (i)

shouxiang = 1
cha = 3
geshu  = 1
sum = 0
#for i in range(100):
while geshu <= 100:
	sum = sum + shouxiang
	shouxiang = shouxiang + cha
	geshu  = geshu + 1	
print (sum)


suibian = ['nishuoshenmne','woxihuan',2001,'shide']
print (suibian)
del suibian[1]
suibian[1] = 'meiguanxi'
print (suibian)

#这是一个python字典
zidian = {'first':'name','last':'name',"sex":'man'}
for x in zidian:
	print (x)
print (zidian['first'])

import time
localtime = time.asctime(time.localtime(time.time()))
print ('现在的时间是：',localtime)

import calendar
calendar = calendar.month(2016,7)
print (calendar)

def printme(str):
	print (str)
	return

printme ("ziji jiejue")
printme ("nigenwoshuoshuo")

'''
def sum(x1,x2):
	total = x1 + x2
	return total
total  = sum(1,2)
print (total)
'''
money = 2000
def addmoney():
	global money
	money = money + 1

print (money)
addmoney()
print (money)

#print (globals())
import math

#str1 = input('请输入：')
#print ('你输入的内容是：', str1)

sum2 = 0
x2 = 1
while x2 <= 100:
	if x2 % 2 != 0:
		sum2 = sum2 + x2
	x2 = x2 + 1
print (sum2)

sum1 = 0
x = 1
n = 1
while True:
    if n > 20:
        break
    sum1 = sum1 + x
    n = n + 1
    x = x + 1
print (sum1)

sum3 = 0
x3 = 0
while True:
    x3 = x3 + 1
    if x3 > 100:
    	break
    if x3 % 2 == 0:
    	continue 
    sum3 = sum3 + x3
print (sum3)

for x4 in [1,2,3,4,5,6,7,8,9]:
	for x5 in [0,1,2,3,4,5,6,7,8,9]:
		if x4 < x5:
			print (x4*10+x5)

#def square_of_sum(L):
#	sum = 0
#	for x in L:
#		sum = sum + x * x
#	return sum
#print square_of_sum([1, 2, 3, 4, 5])
#print square_of_sum([-5, 0, 5, 15, 25])

def move(n, a, b, c):
    if n ==1:
        print (a, '-->', c)
        return
    move(n-1, a, c, b)
    print (a, '-->', c)
    move(n-1, b, a, c)
move(4, 'A', 'B', 'C')

def greet(n = 'world'):
	n1 = input('please enter:')
	if n1 == '':
		print ('hello,'+''+n)
	else:
		print ('hello,'+''+n1)

L = range(1, 101)

print (L[:10])
print (L[::2])
print (L[:50:3])

