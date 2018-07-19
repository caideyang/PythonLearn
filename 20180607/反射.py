#encoding:utf-8

class BlackMedium:
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr

    def sell_house(self):
        print("[%s]正在卖房" % self.name)

    def rent_house(self):
        print("[%s]正在卖房" % self.name)



if __name__ == "__main__":
    b1 = BlackMedium('链家','华龙小区')

    # print(hasattr(b1,'name'))
    # print(hasattr(b1,'name1'))
    # print(getattr(b1,'name1','No this attr'))
    # setattr(b1,'name1','fuck')
    # delattr(b1,'name1')
    # print(b1.__dict__)
    # print(getattr(b1, 'name1', 'No this attr'))

    # print(hasattr(b1,'rent_house'))
    # print(getattr(b1,'rent_house'))
    # func = getattr(b1,'rent_house')
    # func()
    # setattr(b1,'func1',func)
    # b1.func1()
    # setattr(b1,'func2',lambda x:x+1)
    # print(b1.__dict__)
    # print(b1.func2(10))

    # setattr(b1,'func2',lambda self:self.name+"sb")
    # print(b1.__dict__)
    # print(b1.func2(b1))