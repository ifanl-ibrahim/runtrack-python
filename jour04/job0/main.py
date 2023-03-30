n = int(input("Entrez un nombre entier : "))

def factor(n):
    if (n == 0):
        return 1
    else:
        return n * factor(n-1)
    
print('Le factoriel de', n, 'est', factor(n))