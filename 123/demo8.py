import re
#验证座机号码的正则
'''
data = input('请输入电话：')
if re.match(r'\d{4}\-\d{7}',data):
	print ('OK')
else:
	print ('WRONG')
'''
#验证编码的正则
'''
data1 = input('请输入编码：')
if re.match(r'[A-Z\_A-Z]',data1):
	print ('编码正确')
else:
	print ('编码不正确')
'''	
#验证邮箱的正则
'''
data2 = input('请输入邮箱：')
if re.match(r'^[a-z1-9A-Z]+\@[a-z1-9A-Z]+.com$',data2):
	print ('正确！')
else:
	print ('错误！')
'''
#验证手机号的正则
'''
data3  = input('请输入手机号：')
if re.match(r'^1(3|4|5|7|8)\d{9}$',str(data3)):
	print ('正确的手机号!')
else:
	print ('错误的手机号')
'''
#正则练习
'''
data4 = input('请输入：')
if re.match(r'^\d{3}.com$',data4):
	print ('right')
else:
	print ('wrong')
'''

list1 = 'a b b       c'
print (list1)
list2 = list1.split()
print (list2)
