def fonction(a,b):
    n=int(0)
    while (n+1)*a<b :
        n=n+1
    multiple=n*a
    plusgrandmultiple=multiple
    reponse=("le plus grand multiple de a inferieur a b est " , plusgrandmultiple)
    return reponse

c=int(input("qui est c ?"))
d=int(input("qui est d ?"))

print(fonction(c,d))