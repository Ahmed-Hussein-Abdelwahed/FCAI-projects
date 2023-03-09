# to show attributes of returned object [contains public, protected, or private attributes]
# you must write function inside the class to show these attributes
# otherwise you will print the attributes addresses only
class T:
    def __init__(self):
        self.__o = 0
        self.__p = ''

    def mod(self):
        self.__o = input('Enter o value')
        self.__p = input('Enter p value')
        return self

    def show(self):
        print('o = ', self.__o)
        print('p = ', self.__p)


op = T()
op2 = op.mod()
print('op==>')
op.show()
print('op2 ==>')
op2.show()
