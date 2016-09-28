from demo2 import file_in
from demo2 import zhuanhuan
import os

sarah = file_in("sarah2.txt")
print (sarah)
#使用最普通的赋值办法将得到的数组分离，在对需要的数据进行处理
'''
sarah_name = sarah.pop(0)
sarah_bir = sarah.pop(0)
print (sarah)
print (sarah_name + "最快的成绩是：",end = " ")
print (sorted(set([zhuanhuan(i) for i in sarah]))[0:3])
'''
#使用字典将分开的数据整合至一起，方便后续使用
'''
sarah_new = {
	'name':sarah.pop(0),
	'birthday':sarah.pop(0),
	'chengji':sarah
}
print (sarah_new['name']+'的成绩是：'+str(sorted(set([zhuanhuan(i) for i in sarah_new['chengji']]))[0:3]))
'''
#使用改进后的file_in函数，将字典处理逻辑写入file_in函数中，调用函数之后返回一个可以使用的字典
#对得到的数据稍加处理，即可直接打印
#file_in方法直接写死字典逻辑以及读取文件的方法，对未知的输入文件或不止一行的输入文件，file_in不在适用
print (sarah['name'] + '成绩是：' + sarah['cj'])

class people:
	def __init__(self,value = 0):
		self.thing = value
	def how_long(self):
		return len(self.thing)

a = people("haha")
print (a.how_long())

class player:
	def __init__(self,p_name,p_bir = None,p_times = []):
		self.name = p_name
		self.bir = p_bir
		self.times = p_times
james = player("james",'2016-01-01',['2.11','2.12','2.13'])
print (james.name,james.bir,james.times)

