# How to define Python classes
# Example file for working with classes
class myClass():
    def method1(self):
        print ("Amala")

    def method2(self, someString):
        print("Name:" + someString)


def main():
    # exercise the class methods
    c = myClass()
    c.method1()
    c.method2(" Amala is fun")


if __name__ == "__main__":
    main()