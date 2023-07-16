from math import sqrt
def fonction(a):
    n=int(0)
    reponse=(a,"est premier")
    for i in range(2,int(sqrt(a))):
        if a%i==0 :
            reponse=(a,"n'est pas premier")
    return reponse

b=int(input("qui est a ?"))
print(fonction(b))

