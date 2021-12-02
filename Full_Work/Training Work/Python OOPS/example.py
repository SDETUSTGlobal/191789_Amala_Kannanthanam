class myClass1():
    def method3(self):
        print ("Amala")

    def method4(self, someString):
        print("Name:" + someString)
class myClass():
    def method1(self):
        print("Amala")
class childClass(myClass):
     #def method1(self):
    # myClass.method1(self);
    # print ("childClass Method1")

    def method2(self):
        print("childClass method2")
def main():
    # exercise the class methods
    c = myClass1()
    c.method3()
    c.method4(" Amala is fun")
    c2 = childClass()
    c2.method1()
    # c2.method2()
if __name__ == "__main__":
    main()