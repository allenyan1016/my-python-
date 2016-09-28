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
yan.sorce  = 50
yan.print_info()
yan.get_grade()
print (yan.get_name())
print (yan.get_sorce())
yan.set_name('zhang')
yan.set_sorce(50)
yan.print_info()
yan.get_grade()
