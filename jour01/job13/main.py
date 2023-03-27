print('Choisissez 5 nombres:')
numbers = []
for i in range(5):
    numbers.append(int(input()))
    numbers.sort()

print('Voici les nombres dans l\'ordre croissant: ', numbers)