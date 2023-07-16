u=[1,1]
def suite (s):
    for i in range(10):
        termesuivant=s[len(s)-2]+s[len(s)-1]
        s.append(termesuivant)
    return s

print(suite(u))