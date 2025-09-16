# class creation
class myClass:

    #private variable
    __privateVar = 27

    #private method
    def __privMeth(self):
        print("i am inside class myClass")

    #function to print value of private variable
    def hello(self):
        print("private variable value: ",myClass.__privateVar)

#object creation and method call
foo = myClass()
foo.hello()
foo.__privMeth            