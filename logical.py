print(3>=3)
un="Admin"
ck="admin"
p=False
print(un==ck)
print(1==1 and 4<3)
print(1==1 or 4<3)
print(un==ck and p)
if un==ck:
    print('succes')
elif 1==1:
    print('maybe')
else:
    print('fail')

s=[1,2,3,4,5]
for i in s:
    print(i**2)

sal={'J':30,'K':40,'L':20}
for s in sal:
    print(f'{s} has salary:{sal[s]}')

mp=[('a',1),('b',2),('c',3)]
for i,j in mp:
    print(f"{i} corresponds {j}")

c=0
c+=1
while c<5:
    print (c)
    c=c+1

for x in range(0,6,2):
    print(x)

print('s' in 'quieuwqueuqwewqeiwqeiw')
print(2 in [1,2,3])
