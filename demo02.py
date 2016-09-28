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

def print_lol(the_list,level=0):
	for i in the_list:
		if isinstance(i,list):
			print_lol(i,level+1)
		else:
			for m in range(level):
				print ('\t',end= '')
			print (i)
print_lol(movies2)
