def hel(n):
    print("Hello "+n+"!")

hel("Cindy")

def addn(n1,n2):
    return(n1+n2)

c=addn(2,5)
print(c)

print(max([1,2,3,4,5]))
print(min([1,2,3,4,5]))

ml=['a','b','c']
i=0
for l,m in enumerate(ml):
    print(f"{m} is at index: {l}")

print("--".join(ml))

def sec(st):
    return "secret" in st.lower()

print(sec("aSecrety"))

def cm(st1):
    o=list(st1)
    for i,l in enumerate(st1):
        for v in "aeiou":
            if l.lower()==v:
                o[i]="x"
    print("".join(o))

cm("Adam")
