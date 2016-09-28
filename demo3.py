import urllib.request

webpage = urllib.request.urlopen('http://www.douban.com')
data = webpage.read()
data1 = data.decode('utf-8')
print (data1)
