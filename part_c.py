
class FaultyCalc:
    pass

class CorrectCalc:
    pass

class MainClass(CorrectCalc, FaultyCalc):
    def __init__(self, x):
        self.x = x

if __name__=="__main__":
    ob1 = MainClass(8.4)
    ob2 = MainClass(0)
    print(ob1 + ob2)
    print(ob1 - ob2)
    print(ob1 * ob2)
    print(ob1 / ob2)
