#简单爬虫，爬取豆瓣网信息，但是失败了

import urllib.request
import urllib.parse
import io 
import sys
import os
####################################################################################################
'''
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
url = 'http://www.douban.com'
#webPage = urllib.request.urlopen(url)
#data = webPage.read()
#代码问题
#data1 = data.decode('utf-8')
with open("爬虫2.txt","w") as f:
	webPage = urllib.request.urlopen(url)
	data = webPage.read()
	data1 = data.decode('utf-8')
	f.write(data1)

print (data1)
print (type(webPage))
print (webPage.geturl())
print (webPage.info())
print (webPage.getcode())
'''
####################################################################################################
'''
url1 = 'http://python.org'
#webHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url1)
webPage = urllib.request.urlopen(req)
data = webPage.read()
data = data.decode('utf-8')
print (data)
'''
####################################################################################################
'''
url = "http://www.d"
user_agent = 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
values = {
	'act': 'login',
	'login[email]':
}
'''
page = urllib.request.urlopen('http://www.douban.com')
data = page.read()
print (data.decode('utf-8'))