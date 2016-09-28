movies = ['the holy grail','the life of brain','the meaning of life']
print (movies[0])
print (movies)
print (len(movies))        #len()方法获取一个列表的长度
movies.append('ceshi1')    #append()方法在列表的末端添加一个数据项
movies.pop()			   #pop()方法在列表的末端删除一个数据项
movies.insert(0,'ceshi2')  #insert()方法在列表的指定位置添加一个数据项
movies.remove('ceshi2')    #remove()方法删除列表一个指定的数据项

movies2 = ['the holy grail',1975,'terry jones & terry gilliam','91 mins',['graham chapman',
			['michael palin','john cleese','terry gilliam','eric idle','terry johns']]]
for i in movies2:
	if isinstance(i,list): #isinstance()方法判断特定数据的特定类型
		for m in i:
			if isinstance(m,list):
				for n in m:
					print (n)
			else:
				print (m)
	else:
		print (i)

def print_lol(the_list,ident=False,level=0):
	for i in the_list:
		if isinstance(i,list):
			print_lol(i,ident,level+1)
		else:
			if ident:
				for m in range(level):
					print ('\t',end= '')
				print (i)
print_lol(movies2)
print_lol(movies2,True)
print_lol(movies2,True,2)

#从标准库中导入OS
import os
#查看当前工作目录是什么
#os.chdir()方法可以改变当前的工作目录
print (os.getcwd())  

#打开一个命名文件，并将文件赋值给一个data文件对象
data = open('demo2.txt') 	
#使用readline()方法从文件获取一个数据行
print (data.readline(),end='')	
print (data.readline(),end="")
#使用seek()方法返回到文件的起始位置，对python的文件也可以使用tell()方法
data.seek(0)	
for i in data:
	print (data.readline(),end="")
#处理完文件之后将文件关闭
data.close()

out = open('demo2.txt',"w")
print ("你在说什么",file = out)
out.close()


