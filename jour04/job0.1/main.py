x = int(input("Entrez un nombre entier : "))
n = int(input("Choisissez la puissance à laquelle vous voulez le multiplier : "))

def puissance(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        y = puissance(x, n/2)
        return y*y
    else:
        return x * puissance(x, n-1)
    
resultat = puissance(x, n)
print("Le résultat de", x, "puissance", n, "est :", resultat)