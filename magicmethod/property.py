class Rectangle(object):

    def __init__(self):
        self.width = 0
        self.height = 0

    def setSize(self, size):
        self.width, self.height = size

    def getSize(self):
        return self.width, self.height

    size = property(getSize, setSize)

    def __setattr__(self, key, value):
        if key == 'size':
            self.size = value
        else:
            self.__dict__[key] = value

    # def __getattr__(self, item):
    #     if item == 'size':
    #         return self.size
    #     else:
    #         raise ValueError

# r = Rectangle()
# r.box = 'abc'
# print r.__dict__['box']
#
# print r.copy

def flatten(nested):

    for sublist in nested:
        for element in sublist:
            yield element

nested = [[1, 2], [3, 4], [5]]
for num in flatten(nested):
    print num

square = [ x*x for x in range(1,10)]
print square

g = ( x*x for x in range(1, 10))
print g.next()
print g.next()
print g.next()
print g.next()
print g.next()
print g.next()
print g.next()
print g.next()
print g.next()
print g.next()
print g.next()

