# Note that
# class A:
#     pass
# class A(object):
#     pass
#
# are the same in python 3 Not in python 2

# overriding method ==>
# ability of any OOP language that allows a subclass to provide a specific
# implementation of a method that is already provided by one of its superclass
# method that has [same name, same parameters or signature, and same return type]


# overloading ==> python by default does not support  method overloading

# polymorphism ==>The word polymorphism means having many forms.
# In programming,polymorphism means the same function name (but different signatures) being used for different types.

class Car(object):
    fuel_type = 'petrol'  # class attribute (static attribute) all objects share the same value of this attribute

    def __init__(self, model, color, maker, price):
        self.model = model
        self.color = color
        self.maker = maker
        self.price = price


ob1 = Car(2014, 'Red', 'Nissan', 10000)
ob2 = Car(2015, 'Blue', 'Honda', 20000)
ob3 = Car(2016, 'Green', 'Toyota', 30000)

print("""For first  car:\nModel:{0.model}\ncolor:{0.color}\nMaker:{0.maker}\nPrice:{0.price}\n
For second car:\nModel:{1.model}\ncolor:{1.color}\nMaker:{1.maker}\nPrice:{1.price}\n
For third car:\nModel:{2.model}\ncolor:{2.color}\nMaker:{2.maker}\nPrice:{2.price}\n""".format(ob1, ob2, ob3))

print(Car.__dict__)  # class attributes information
print(ob1.__dict__)  # object attributes information


