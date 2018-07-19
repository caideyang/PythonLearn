#encoding:utf-8

class Traffic:
    Country = 'China'
    def __init__(self,name,speed,load):
        self.name = name
        self.speed = speed
        self.load = load
    def run(self):
        print("%s is runing" % self.name)


class Subway(Traffic):
    def __init__(self,name,speed,load,line):
        # Traffic.__init__(self,name,speed,load) #调用父类的方法
        super().__init__(name,speed,load)#使用super()方法取代父类名
        self.line = line
    def run(self):
        # Traffic.run(self) #调用父类的方法
        super().run() #使用super()方法取代父类名
        print('%s is runing on speed %s' %(self.name,self.speed))

line13 = Subway("line13",'100km/h',10000,13)
line13.run()