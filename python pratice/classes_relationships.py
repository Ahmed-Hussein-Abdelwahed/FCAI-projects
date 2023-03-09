class Engine:
    def __init__(self, maker, country, cc):
        self.maker = maker
        self.country = country
        self.cc = cc


class Tires:
    def __init__(self, tires_num, size):
        self.number = tires_num
        self.size = size


class Car:
    def __init__(self, name, model, color, maker, country, cc, tires):
        self.name = name
        self.model = model
        self.color = color
        self.engine = Engine(maker, country, cc)  # composition relationships
        self.tires = tires  # aggregation relationship

    def show_info(self):
        print('Name: {}\nModel: {}\nColor: {}'.format(self.name, self.model, self.color))
        print('\nEngine:\nMaker: {}\nCountry: {}\nCCs: {} CC'.format(self.engine.maker, self.engine.country,
                                                                     self.engine.cc))
        print('\nTires:\nNumber:{}\nSize:{}'.format(self.tires.number, self.tires.size))


# Association [has a] including (composition and aggregation):
# You use the parent class features without any modification of the child class

# composition [part of] means that:
# 1. totally dependency
# 2. strong relationship
# 3. when you delete the child class object, Hence the parent class will be deleted automatically
# 4. you create an object class inside the constructor of another class

# Aggregation [has a relationship] means that:
# 1. partially dependency
# 2. when you delete the child class object, Hence the parent class will not be deleted
# 3. you pass an object class to another class

# tire = Tires(10, '20 * 20')
# o = Car('Toyota', 2015, 'Red', 'In-car', 'Japan', 10000, tire)
# o.show_info()

# Inheritance means that:
# You extend the parent class features by child class features
# Python supports multilevel inheritance
# composition and aggregation code is faster than inheritance because of:
# in the inheritance:
# when code wants to end its functionality it founds that he has an inheritance unlike composition and aggregation

class Parent(object):
    def __init__(self, name, country):
        self.father_name = name
        self.country = country

    def display(self):
        print('father name: {}\ncountry: {}'.format(self.father_name, self.country))


class Son(Parent):
    def __init__(self, son_name, father_name, country):
        Parent.__init__(self, father_name, country)
        self.son_name = son_name

    def show_info(self):
        print(f'Son name: {self.son_name}')
        self.display()


son = Son('Ahmed', 'Hussein', 'Egypt')
son.show_info()
