def multiple(c,d):
    if c%d==0 :
        reponse="c est un multiple de d"
        return reponse
        
    else :
        reponse = "c n  est pas un multiple de d"
        return reponse

a=int(input("qui est a ?"))
b=int(input("qui est b ?"))

print(multiple(a,b))