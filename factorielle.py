a=int(input("entre a"))

def factorielle (b):
    i=1
    f=1
    while i!=b :
        i=i+1
        f=f*i
    return f

print(factorielle(a))