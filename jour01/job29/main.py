listNotes = []

def notation(notes):
    for i in notes:
        if (i < 40):
            listNotes.append(i)
        else :
            if ((i + 3) % 5 == 0):
                listNotes.append(i + 3)
            elif ((i + 2) % 5 == 0):
                listNotes.append(i + 2)
            elif ((i + 1) % 5 == 0):
                listNotes.append(i + 1)
            else:
                listNotes.append(i)
    return listNotes

notation([41, 78, 0, 29, 100, 47, 11, 89])
print(listNotes)   