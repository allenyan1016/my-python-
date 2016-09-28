#文件打开联系，使用正常的文件open方法，读取，然后关闭
import os
import pdb

m = open('苗庆新问题.txt')
print (m)

for i in m:
	print (m.readline())

m.close()	

#使用with方法写文件读取，可不用close方法
with open('苗庆新问题.txt') as file:
	for i in file:
		print (i)

#list练习
l = [1,2,3,4,5,6,7,8,9]
#使用max函数打印出l列表的最大的数
print (max(l))
#使用min函数打印书l列表的最小的数
print (min(l))
#重新为l的第一个数赋值
l[0] = 2
print (l)

class name:
	__private = 'siyou'
	private = 'gongyou'
	def print_name(self,name):
		print ('hello,'+name)

name1 = name()
name1.print_name("allen")
print (name1.private)
print (name1._name__private)

list_1 = [1,1,1,1,1,1,1,1,1,1,1]
with open('l.txt','w') as file_l:
	print (list_1,file = file_l)

class Student(object):
    def __init__(self,name,sorce):
        #在属性面前加上__是该属性变为私有属性，无法从外部在改变属性的内容
        self.__name = name;
        self.__sorce = sorce
    def set_name(self,name):
        self.__name = name
    def set_sorce(self,sorce):
        self.__sorce = sorce
    def get_name(self):
        return self.__name
    def get_sorce(self):
        return self.__sorce
    def print_info(self):
        print (self.__name,self.__sorce)
    def get_grade(self):
        if self.__sorce > 60:
            print ('good')
        else:
            print ('bad')

yan = Student('yan',70)
yan.print_info()
yan.get_grade()
yan.name = 'zhang'
pdb.set_trace()
yan.sorce  = 50
yan.print_info()
yan.get_grade()
print (yan.get_name())
print (yan.get_sorce())
yan.set_name('zhang')
yan.set_sorce(50)
yan.print_info()
yan.get_grade()
