import re

regex = r'\b[a-zA-Z]+\b'
def domains():
    with open('data.txt', 'r') as f:
        data = f.read()
        count = 0
        for match in re.finditer(regex, data):
            count += 1
        print(f'Il y a {count} mots sans caractères spéciaux dans le fichier text.txt')

domains()