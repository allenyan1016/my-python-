name = input('please input your name:')
print ('hello',name)

print ('nihao,%s' %('yanzhanghong'))

x1 = 72
x2 = 85
r = (x2-x1)/x1*100
print ('提升的百分点是：%.1f %%' %(r))

l = [1,2,3,4,5,6,7,8,9]
print (l[len(l)-1])

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print (L[0][0])
print (L[1][1])
print (L[2][2])

height = 1.75
weight = 80.5
BMI = weight**2/height
if BMI < 18.5:
	print ('过轻')
elif BMI >= 18.5 and BMI < 25:
	print ('正常')
elif BMI >= 25 and BMI < 28:
	print ('过重')
elif BMI >= 28 and BMI < 32:
	print ('肥胖')
elif BMI >= 32:
	print ('过渡肥胖') 

L = ['Bart', 'Lisa', 'Adam']
for i in L:
	print ('hello',i)

def power(x,n=2):
	return x**n
print (power(5,2))
print (power(5,3))
print (power(5))

def power_2(*nums):
	sum = 0
	for i in nums:
		sum =sum + i**2
	return sum

print (power_2(1,2,3,4,5,6,7,8,9))
print (power_2(*l))

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print (L2)

d = {'x': 'A', 'y': 'B', 'z': 'C' }
L3 = [x+'='+y for x,y in d.items()]
print (L3)

def lib(max):
	x,y,z = 0,0,1
	while x < max:
		print (z)
		y,z = z,y+z
		x=x+1
	return 'done'
print (lib(6))

def add(x,y,z):
	return f(x) + f(y)
f = abs
print (add(-5,6,f))

ex = ['adam','LISA','barT']
def daxie(m):
	#for i in m:
	#return m.title()
	for i in m:
		i[0].upper() + i[1:].lower()
		print (i)

l1 = list(map(daxie,ex))
print (l1)

from functools import reduce
def qiuji(x,y):
	return x*y
print ('3*5*7*9 = ',reduce(qiuji,[3,5,7,9]))

def jishu(s):
	return s % 2 == 1
print (list(filter(jishu,l)))

def qbl(m):
	x,y,z = 0,0,1
	while x < m:
		#print (z)
		yield b
		y,z = z,y+z
		x=x+1
	print ('gaoding')
qbl(10)

ex2 = ['adam','LISA','barT']
ex3 = {0: "abc", 1: 123, 2: "de6"}
def daxie2(m):
	if type(m) == {}.__class__:
		m = m.values()

	#for i in m:
	#return m.title()
	po = []
	for i in m:
		a = str(i)[0].upper() + str(i)[1:].lower()
		po.append(a)
	print(po)
daxie2(ex2)
daxie2(ex3)

def my_abs(x):
	if x >= 0:
		return x
	elif x < 0:
		return -x
print (my_abs(6))
print (my_abs(-5))