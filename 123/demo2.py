import os
#未定义文件处理函数时需进行四次文件打开与处理的操作
'''
with open('james.txt') as jaf:
	data = jaf.readline()
james = data.strip().split(',')
with open('julie.txt') as juf:
	data = juf.readline()
julie = data.strip().split(',')
with open('wikey.txt') as wif:
	data = wif.readline()
wikey = data.strip().split(',')
with open('sarah.txt') as saf:
	data = saf.readline()
sarah = data.strip().split(',')
'''
#将转换逻辑写入函数中，只需调用该函数即可完成对数据的统一
def zhuanhuan(list_in):
	if '-' in list_in:
		splitter = '-'
	elif ':' in list_in:
		splitter = ':'
	else:
		return list_in
	(mins,secs) = list_in.split(splitter)
	return (mins + '.' + secs)
#定义函数，处理读到的文件，并返回已经处理的好的转换为列表的文件，对文件行数多余1的文件并不适用
def file_in(x):
	with open (x) as file:
		data = file.readline()
		file_1 = data.strip().split(',')
	return ({
		'name' : file_1.pop(0),
		'birthday' : file_1.pop(0),
		'cj' : str(sorted(set([zhuanhuan(i) for i in file_1]))[0:3])
		})

james = file_in("james.txt")
julie = file_in("julie.txt")
sarah = file_in("sarah.txt")
wikey = file_in("wikey.txt")
'''
print (sorted(set([zhuanhuan(i) for i in james]))[0:3])
print (sorted(set([zhuanhuan(i) for i in julie]))[0:3])
print (sorted(set([zhuanhuan(i) for i in sarah]))[0:3])
print (sorted(set([zhuanhuan(i) for i in wikey]))[0:3])
'''
#未定义处理函数时，需先定义四个空数组，并将处理过的数据插入新的空数组中
'''
clean_james = []
clean_julie = []
clean_wikey = []
clean_sarah = []
for i in james:
	clean_james.append(zhuanhuan(i))
for i in julie:
	clean_julie.append(zhuanhuan(i))
for i in wikey:
	clean_wikey.append(zhuanhuan(i))
for i in sarah:
	clean_sarah.append(zhuanhuan(i))

clean_james = [zhuanhuan(i) for i in james]
clean_sarah = [zhuanhuan(i) for i in sarah]
clean_wikey = [zhuanhuan(i) for i in wikey]
clean_julie = [zhuanhuan(i) for i in julie]
ununique_james = []
ununique_julie = []
ununique_wikey = []
ununique_sarah = []
for i in clean_james:
	if i not in ununique_james:
		ununique_james.append(i)
for i in clean_julie:
	if i not in ununique_julie:
		ununique_julie.append(i)
for i in clean_wikey:
	if i not in ununique_wikey:
		ununique_wikey.append(i)
for i in clean_sarah:
	if i not in ununique_sarah:
		ununique_sarah.append(i)
print (sorted(ununique_james)[:3])
print (sorted(ununique_julie)[:3])
print (sorted(ununique_wikey)[:3])
print (sorted(ununique_sarah)[:3])
print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_sarah))
print(sorted(clean_wikey)) 
print (sorted(set(clean_james))[:3])
'''