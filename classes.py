# Example file for working with classes

class myClass():
    def method1(self):
        print "myClass method1"

    def method2(self, someString):
        print "myClass method: " + someString

def main():
    #exercise the class methods
    c = myClass()
    c.method1()
    c.method2("This is a string")

if __name__ == "__main__":
    main()
