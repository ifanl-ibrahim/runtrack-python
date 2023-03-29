import re

def domains():
    print('renseigner le nombre de lettre que vous voulez par mot')
    nb = int(input())
    regex = r'\b[a-zA-Z]{'+str(nb)+r'}\b'
    with open('data.txt', 'r') as f:
        data = f.read()
        count = 0
        for match in re.finditer(regex, data):
            count += 1
        print(f'Il y a {count} mots de {nb} dans le fichier text.txt')

domains()