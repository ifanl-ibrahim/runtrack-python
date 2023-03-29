import re

regex = r'\b\w+\.(?:\w{2,3}\.?){1,2}\b'
def domains():
    with open('domains.xml', 'r') as f:
        data = f.read()
        count = 0
        for match in re.finditer(regex, data):
            count += 1
            print(f'Extension trouvée: {match.group()}')
        print(f'Il y a {count} extension domaines dans le fichier domains.xml')

domains()