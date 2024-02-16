#two.py
import one

print("Top level in 2.py")

one.func()

if __name__=="__main__":
    print("2.py is being run directly")
else:
    print("2.py has been imported")
