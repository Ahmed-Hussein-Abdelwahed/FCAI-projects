# for private attributes you can not show any variable unless you you use a class method to do that job
# if don't use a class method to show variable you will show the address of that variable only

class A:
    def __init__(self, number, string):
        self.__number = number
        self.__string = string

    def show(self):
        print('number = ', self.__number)
        print('string = ', self.__string)


o1 = A(10, 'ahmed')
o2 = A(15, 'Hussein')

u = [o1, o2]

for i in u:
    i.show()


# for protected attributes you can not show any variable unless you you use a class method to do that job
# if don't use a class method to show variable you will show the address of that variable only

class B:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def show(self):
        print('x = ', self._x)
        print('y = ', self._y)


ob1 = B('hazem', 10)
ob2 = B('helal', 36)
p = [ob1, ob2]

for i in p:
    i.show()


# for public attributes you can show any variable outside the class

class C:
    def __init__(self, o, r):
        self.o = o
        self.r = r

    def show(self):
        print('o = ', self.o)
        print('r = ', self.r)


obj1 = C('hamed', 56)
obj2 = C('hamza', 78)
l = [obj1, obj2]

for i in l:
    print(i.o)
    print(i.r)
