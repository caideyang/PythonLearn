#encoding:utf-8

import abc


class HardWare(metaclass=abc.ABCMeta):
    """
    引入abc，通过@abc.abstractmethod装饰器来限制所有的子类都得继承父类的抽象类
    """

    @abc.abstractmethod
    def read(self):
        pass

    @abc.abstractmethod
    def write(self):
        pass

    def test(self):
        print("Hello !")


class Mem(HardWare):

    def read(self):
        print("mem read")

    def write(self):
        print("mem write")

mem = Mem()
mem.test()