# -*- coding: utf-8 -*-  
#使用爬虫爬取小说  
import urllib 
import re  
import chardet  
  
  
class Book_Spider:  
  
    def __init__(self):  
        self.pages = []  
  
    # 抓取一个章节  
    def GetPage(self):  
        myUrl = "http://www.zhuzhudao.com/txt/1/1/";  
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
        headers = { 'User-Agent' : user_agent }  
        request = urllib2.Request(myUrl, headers = headers)  
        myResponse = urllib2.urlopen(request)  
        myPage = myResponse.read()  
  
        #先检测网页的字符编码,最后统一转为 utf-8  
        charset = chardet.detect(myPage)  
        charset = charset['encoding']  
        if charset == 'utf-8' or charset == 'UTF-8':  
            myPage = myPage  
        else:  
            myPage = myPage.decode('gb2312','ignore').encode('utf-8')  
        unicodePage = myPage.decode("utf-8")  
  
        try:  
            #抓取标题  
            my_title = re.search('<h1>(.*?)</h1>',unicodePage,re.S)  
            my_title = my_title.group(1)  
        except:  
            print ('标题 HTML 变化，请重新分析！')  
            return False  
          
        try:  
            #抓取章节内容  
            my_content = re.search('<div.*?id="htmlContent" class="contentbox">(.*?)<div',unicodePage,re.S)  
            my_content = my_content.group(1)  
        except:  
            print ("内容 HTML 变化，请重新分析！")  
            return False  
          
        #替换正文中的网页代码  
        my_content = my_content.replace("<br />","\n")  
        my_content = my_content.replace(" "," ")  
  
        #用字典存储一章的标题和内容  
        onePage = {'title':my_title,'content':my_content}  
        return onePage  
  
  
    # 用于加载章节  
    def LoadPage(self):  
        try:  
            # 获取新的章节  
            myPage = self.GetPage()  
              
            if myPage == False:  
                print ('抓取失败！')  
                return False  
              
            self.pages.append(myPage)  
        except:  
            print ('无法连接服务器！')  
  
    #显示一章  
    def ShowPage(self,curPage):  
            print (curPage['title'])  
            print (curPage['content'])  
  
    def Start(self):  
        print (u'开始阅读......\n')  
        #把这一页加载进来  
        self.LoadPage()  
        # 如果self的pages数组中存有元素  
        if self.pages:  
            nowPage = self.pages[0]  
            self.ShowPage(nowPage)  
  
  
#----------- 程序的入口处 -----------  
print (u)""" 
--------------------------------------- 
   程序：阅读呼叫转移 
   版本：0.1 
   作者：angryrookie 
   日期：2014-07-05 
   语言：Python 2.7 
   功能：按下回车浏览章节 
--------------------------------------- 
"""  
  
print (u)'请按下回车：'  
raw_input()  
myBook = Book_Spider()  
myBook.Start()  