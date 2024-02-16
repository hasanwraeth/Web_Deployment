x='outside' #global
def report():
    x='inside'#local
    return x

print(x)
print(report())

#LEGB Local Enclosing Global Built-in
def enclo():
    x='Enclosing'#enclosing
    def report():
        #x='local'#local
        print(x)
    report()
enclo()

x='outside' #global
def report():
    global x
    x='inside'#local
    return x

print(x)

ml=[1,2,3,4]

print(type(ml))

class Sample(object):
    pass
x=Sample()
print(type(x))

class Dog(object):
    """docstring for Dog."""
    #Class Object Attribute
    species = 'mammal'
    def __init__(self, b1, n1):
        self.b = b1
        self.n = n1
x=Dog('lab','Sam')
y=Dog('gold','Cin')
print(type(x))
print(x.b, x.n, x.species)
print(y.species, y.n)

class Circle(object):
    """docstring for Circle."""
    pi=3.14
    def __init__(self, r1='Lam'):
        self.r = r1
    def a1(self):
        return self.pi*self.r**2
    def c1(self):
        return self.pi*self.r*2

mc=Circle(10)
print(mc.r, mc.pi, mc.a1(), mc.c1())

class Animal():
    """docstring for Animal."""

    def __init__(self,fur):
        self.fur = fur
    def report(self):
        print('Animal')
    def eat(self):
        print('Eating')

#a=Animal()
#a.eat()

class Dog(Animal):
    """docstring for Dog."""

    def __init__(self,fur):
        Animal.__init__(self,fur)
        print('Dog created')
    def report(self):
        print("Dog!")

d=Dog('Bushy')
d.eat()
d.report()

class Book(object):
    """docstring for Book."""

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self):
        return f"Title: {self.title} Author: {self.author}"
    def __len__(self):
        return self.pages
    def

mb=Book("Python Rocks!", 'Hasan', 69)
print(mb)
print(len(mb))
