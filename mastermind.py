essai=0
tentativesdereussir=[]
print("Le but du jeu est de trouver la bonne combinaison de couleurs : ordre des couleurs et couleurs différentes")
print("Il y a 4 couleurs différentes possibles : bleu, noir, rouge et vert")
print("Tu as 12 essais pour trouver la bonne combinaison")
print(" il y a  4 emplacements de couleurs")


emplacement1=input("donner le nom de la couleurs du 1er emplacement en minuscules et sans espaces ")
emplacement2=input("donner le nom de la couleurs du 2eme emplacement ")
emplacement3=input("donner le nom de la couleurs du 3eme emplacement ")
emplacement4=input("donner le nom de la couleurs du 4eme emplacement ")
couleursàtrouver=[emplacement1 , emplacement2 , emplacement3 , emplacement4]

while essai<12:

def couleursjustes(liste):
    nombresdecouleursjustes=0
    for i in range(len(liste)):
        if liste[i]=couleuràtrouver[i]:
           nombresdecouleursjustes=nombresdecouleursjustes+1
