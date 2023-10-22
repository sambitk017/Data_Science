class Father:
  def __int__(self):
    Ch =Child1(self)         ####
    Ch.house_prop2()
  @staticmethod
  def house_prop1():
    print("House prop 1")


Father.house_prop1()

class Child1:
    def __init__(self, parent):
        self.parent = parent

    @staticmethod
    def house_prop2():
        print("House prop 2")