#показывает заметки
notes = []
if len(notes) == 0:
    print("Немає нотаток")
else:
    print("\nСписок нотаток:")
    for note in notes:
        print(note)


# добавляет заметки
def addNote():

    noteToAdd = input("Введіть текст нотатки: ")
    notes.append(noteToAdd)
    print("\nНотатка додана успішно!")
    return notes
# сохраняет файл
def write_notes():
    with open("note.txt", "w") as f:
        f.write(str(notes) + "\n")
        print("\nФайл збережено! ")
        f.close()

# должен открывать файл для чтения, но не выходит
def open_note():
    with open(input('Введите точное имя файла:'), "r") as f:
        f.read()




# удаляет заметки
def deleteNote():
    noteToDelete = input("Введіть текст нотатки для видалення: ")
    if noteToDelete in notes:
        notes.remove(noteToDelete)
        print("\nНотатка видалена успішно!")
    else:
        print("\nТака нотатка не знайдена!")
# показывает рание заметки
def earliestNotes():
        earliestNotes = sorted(notes, key=str or float)
        for note in earliestNotes:
            print(note)
# показывает позние заметки
def latestNotes():
    latestNotes = sorted(notes, key=str or float, reverse=True)
    print("\nНайпізніші нотатки:")
    for note in latestNotes:
        print(note)
# показывает заметки от длыных до коротких
def longestNotes():
    longestNotes = sorted(notes, key=len, reverse=True)
    print("\nНайдовші нотатки:")
    for note in longestNotes:
        print(note)
# показывает от коротких к длинным
def shortestNotes():
    shortestNotes = sorted(notes, key=len)
    print("\nНайкоротші нотатки:")
    for note in shortestNotes:
        print(note)
# это цикл для показа вариаций выбора
notes = []
while True:
    choice = input("\nЩо ви хочете зробити? \n[1] Відобразити нотатки \n[2] Додати нотатку \n[3] Видалити нотатку \n[4] Найраніші нотатки \n[5] Найпізніші нотатки \n[6] Найдовші нотатки \n[7] Найкоротші нотатки \n[8] Вiдкрити файл для читання  \n[q] Вийти \n ")
    if choice == '1':
        print('|'.join(notes))
    elif choice == '2':
        addNote()
    elif choice == '3':
        deleteNote()
    elif choice == '4':
        earliestNotes()
    elif choice == '5':
        latestNotes()
    elif choice == '6':
        longestNotes()
    elif choice == '7':
        shortestNotes()
    elif choice == '8':
        open_note()
    elif choice == 'q':
        write_notes()
        break
    else:
        print("Введіть правильний варіант!")


