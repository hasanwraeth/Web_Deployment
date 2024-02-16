def h(name='Jose'):
    print("h() function run!")
    def g():
        return "    This is inside g()"
    def w():
        return "    This is inside w()"
    if name=="Jose":
        return w()
    else:
        return g()

x=h("Sam")
print(x)

def h1():
    return " Hi Hasan"
def other(func):
    print("some other code")
    print(func())

other(h1)

def new_d(func):
    def wrap_f():
        print("some code before exe func")
        func()
        print("other code after exe func")
    return wrap_f

@new_d #== f_nds_dec=new_d(f_nds_dec)
def f_nds_dec():
    print("Dec me!")

f_nds_dec()

#f_nds_dec=new_d(f_nds_dec)

f_nds_dec()
