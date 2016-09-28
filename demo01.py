#题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
for x in range(1,5):
	for y in range(1,5):
		for z in range(1,5):
			if x!=y and x!=z and y!=z:
				print (x*100+y*10+z)

#题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，
#高于10万元的部分，可可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到
#100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
str1 = int(input('请输入利润：'))
#jisuan(str)
#def jisuan(str):
if str1 <= 100000:
	str1 = str1 * 0.1
elif str1 > 100000 and str1 <= 200000:
	str1 = 100000 * 0.1 + (str1 - 100000)*0.075
elif str1 > 200000 and str1 <= 400000:
	str1 = 100000 * 0.1 + (str1 - 100000)*0.075 + (str1 - 200000) * 0.05
elif str1 > 400000 and str1 <= 600000:
	str1 = 10000 * 0.1 + (str1 - 100000)*0.075 + (str1 - 200000) * 0.05 + (str1 - 400000) * 0.03
elif str1 > 600000 and str1 <= 1000000:
	str1 = 10000 * 0.1 + (str1 - 100000)*0.075 + (str1 - 200000) * 0.05 + (str1 - 400000) * 0.03 + (str1 - 600000) * 0.015
elif str1 > 1000000:
	str1 = str1 * 0.1 + (str1 - 100000)*0.075 + (str1 - 200000) * 0.05 + (str1 - 400000) * 0.03 + (str1 - 600000) * 0.015
	+ (str1 - 1000000) * 0.001
print (str1)

#一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？
#可以引用math，使用sqrt方法
for i in range(1,10000):
	x = int((i+100)**0.5)
	y = int((i+268)**0.5)
	if (x**2 == i+100) and (y**2 == i+268):
		print (i)
	#if str(x).split(".")[1] == "0" and str(y).split(".")[1] == "0":
	#	print(i)

#输入某年某月某日，判断这一天是这一年的第几天？
str2 = input("请输入年月日(YYYY/MM/DD)：")
year = int(str2.split("/")[0])
month = int(str2.split("/")[1])
day = int(str2.split("/")[2])
tian = 0
i = 0
days1 = [31,28,31,30,31,30,31,31,30,31,30,31]
days2 = [31,29,31,30,31,30,31,31,30,31,30,31]
if (year%4 == 0 and year%100 != 0) or year%400 == 0 :
	if month == 1:
		print ("这是",year,"年的第",day,"天")
	if month > 1 and month <= 12:
		while i < (month-1):
			tian = tian + days2[i]
			i =i + 1
		tian = tian + day
		print ("这是",year,"年的第",tian,"天")
if year%4 != 0 and year%400 != 0:
	if month == 1:
		print ("这是",year,"年的第",day,"天")
	if month > 1 and month <= 12:
		while i < (month-1):
			tian = tian + days1[i]
			i =i + 1
		tian = tian + day
		print ("这是",year,"年的第",tian,"天")
		#print("这是{0}年的第{1}天".format(year, tian))

#输入三个整数x,y,z，请把这三个数由小到大输出。
str3 = input("请输入三个数（x,y,z）：")
x = int(str3.split(",")[0])
y = int(str3.split(",")[1])
z = int(str3.split(",")[2])
m = [x,y,z]
m.sort()
print (m)

#将一个列表的数据复制到另一个列表中。
list1 = [344,23,423,4,234,23,423,4,234,23]
list2 = list1[:]
print (list2)

#输出9*9乘法口诀表。
for i in range(1,10):
	for m in range(1,i+1):
		print (i * m,'=',i,'*',m,end=" ")
	print()

#暂停一秒输出。
import time
list3 = [123,123,12,423,4,235,23]
for i in list3:
	print (i)
	time.sleep(1)

#判断101-200之间有多少个素数，并输出所有素数。
total = 0
for i in range(101,201):
	for m in range(2,i):
		if i%m == 0:
			break
	total = total + 1
print ('素数的总数是：',total)

#打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，
#因为153=1的三次方＋5的三次方＋3的三次方。
for i in range(100,1000):
	x = i / 100
	y = i % 100 / 10
	z = i % 100 % 10
	if i == x**3 + y**3 + z**3:
		print (i)

#将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
