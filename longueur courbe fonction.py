a=int(input("entre a"))
b=int(input("entre b"))
from math import sqrt
def longueur (c,d):
    l=0
    if c<d :
        i=a
        for i in range(c,d):
            i=i+0.01
            l=sqrt((d-c)*(d-c)+(sqrt(d)-sqrt(c))*(sqrt(d)-sqrt(c)))

    return l

print(longueur(a,b))
