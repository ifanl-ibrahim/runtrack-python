def thePower():
    print('Entrer une chaine de caractères')
    w = open('output.txt', 'w')
    w.write(input())
    w.close()

thePower()