#encoding:utf-8

class H2O:
    def __init__(self,name,temp):
        self.name = name
        self.temp = temp
    def turn_ice(self):
        if self.temp < 0:
            print("冰，温度%s ℃" % self.temp)
        elif self.temp >= 100:
            print("水蒸气 温度%s ℃" %self.temp)
        else:
            print("水 温度%s ℃" %self.temp)

class Water(H2O):
    def __init__(self,name,temp):
        super().__init__(name,temp)

class Ice(H2O):
    def __init__(self,name,temp):
        super().__init__(name,temp)

class Stream(H2O):
    def __init__(self,name,temp):
        super().__init__(name,temp)

water = Water("水",45)
water.turn_ice()
ice = Ice("冰",-10)
ice.turn_ice()
stream = Stream('水蒸气',200)
stream.turn_ice()

def turn_ice(obj):
    obj.turn_ice()

turn_ice(water)
turn_ice(ice)
turn_ice(stream)