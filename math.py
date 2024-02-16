print("hello world")
print(2+1)
#PEP best standard practices in python
a=10
a=a+a
print(a)
pup=6
wt=2
total = pup*wt
print(total)
a="Hello"
print(len(a))
#indexing
print(a[0:4])
#slicing, excluding stop index
a="abcdeefghij"
print(a[0:4:2])
print(a+" "+a)
print(a.upper())
b="Hello World"
print(b.split("o"))
u="Sam"
color="red"
print("{}'s favorite color is {}".format(u,color))
print(f"{u}'s favorite color is {color}")
#Lists
ml=[1,2,3,4,5,6,7.7,"Sam"]
ml.append('z')
ml.insert(0,'a')
pop1=ml.pop(0)
print(ml)
print(ml[3::2])
print(pop1)
nl=[0,1,2, ml]
print(nl)
print(nl[3][4])
d1={'x':1,'y':[2,3,4]}
d1['z']={'s':30,'t':100}
print(d1)
d1['x']=d1['x']+4
print(d1['x'])
print(d1['y'][1])
print(d1['z']['t'])
#d.keys(), d.values(), d.items()
#tuples
t1=(1,2,3,4,5)
print(t1[4])
#sets
s1=set()
s1.add(1)
s1.add(2)
s1.add(3)
s1.add(4)
s1.add(4)
print(s1)
l1=[1,1,1,2,2,3,4]
print(set(l1))
#Booleans
a=True
b=False
c=None
print(a,b,c,1>2)
