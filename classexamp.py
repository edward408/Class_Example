#Example of a simple Python class

class Employee:
    empCount = 0
    #class variable whose variable is shared among all instances of a this class.
    #This can be accessed as Employee.empCount from inside the class or outside the class.

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount+=1
    #init is a special method, called class constructor or initialization method when a new instance of this class is created.
    #You declare other class methods like normal functions with the exception that the first argument to each method is self.

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name: ", self.name, ", Salary:", self.salary


#To create instances of a class, you call the class using class name and pass it in whatever arguments its __init__method accepts
emp1 = Employee("Zara",2000)
emp2 = Employee("Manni", 5000)

#You access the objects attributes using the dot operator with object. Class variable would be accessed using class name as follows
emp1.displayEmployee()
emp2.displayEmployee()
print "Total employee %d" % Employee.empCount

#You can add, remove, or modify attributes of classes and objects at any time-
emp1.age = 7
emp1.age = 8

#Instead of using the normal statements to access attributes, you can use these functions
print getattr(emp1,'age')
print hasattr(emp1,'age')

#Every python class keeps following built-in attributes and they can be accessed
#with dot operators like any other attribute

#Garbage collection: When an objects reference count reaches zero,
#Python collects it automatically

#Ideally, you should define your classes in seperate file, then you should import them
# in your main program file using import statement

