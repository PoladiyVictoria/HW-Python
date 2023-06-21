# Задача 38: Создать телефонный справочник возможностью добавления записей и чтения. 
# Пользователь также может ввести фамилию, тогда программа должны вывести на экран все записи с этой фамилий. 
# Также пользователь может добавлять новых людей в справочник в режиме экспорт.

def Read_phonebook():
    print('Как вы хотите искать?')
    mod1 = int(input('1 - по человеку, 2 - по № телефона: '))
    with open('E:\Домашка\HW Python\Task38\phonebook.txt', 'r', encoding='utf-8') as f_read:
        book = f_read.read().splitlines()
        if mod1 == 1:
            human = input('Введите фамилию, имя или отчество: ')
            for person in book:
                some_man = person.split(':')
                buf = some_man[0]
                if buf == human:
                    print(person)
                else:
                    name = buf.split()
                    for partname in name:
                        if partname == human:
                            print(person)
        elif mod1 == 2:
            num = input('Введите номер телефона: ')
            for person in book:
                some_man = person.split(':')
                number = str(some_man[1])
                if number == num:
                    print(person)

def Entry_phonebook():
    with open('E:\Домашка\HW Python\Task38\phonebook.txt', 'a', encoding='utf-8') as f_entry:
        print('Введите нового абонента:')
        name = input('Введите Ф.И.О: ')
        number = input('Введите номер телефона: ')
        f_entry.writelines('\n')
        f_entry.writelines(f'{name}: {number}')

def Change_phonebook():
    print('Что вы хотите изменить?')
    mod1 = int(input('1 - человека, 2 - № телефона: '))
    with open('E:\Домашка\HW Python\Task38\phonebook.txt', 'r', encoding='utf-8') as f_change:
        book = f_change.read().splitlines()
        book = list(book)
        human = input('Введите фамилию, имя или отчество: ')
        for person in book:
            some_man = person.split(':')
            buf = some_man[0]
            number = str(some_man[1])
            if buf == human:
                if mod1 == 1:
                    new_man = input('Введите новое Ф.И.О: ')
                    book.remove(person)
                    person = new_man + ': ' + number
                    book.append(person)
                if mod1 == 2:
                    new_num = input('Введите новый номер: ')
                    book.remove(person)
                    person = buf + ': ' + new_num
                    book.append(person)
            else:
                name = buf.split()
                for partname in name:
                    if partname == human:
                        if mod1 == 1:
                            new_man = input('Введите новое Ф.И.О: ')
                            book.remove(person)
                            person = new_man + ': ' + number
                            book.append(person)
                        if mod1 == 2:
                            new_num = input('Введите новый номер: ')
                            book.remove(person)
                            person = buf + ': ' + new_num
                            book.append(person)
        with open('E:\Домашка\HW Python\Task38\phonebook.txt', 'w', encoding='utf-8') as f_change1:
            for person in book:
                if person == book[0]:
                    f_change1.writelines(person)
                else:
                    f_change1.writelines('\n')
                    f_change1.writelines(person)

def Remove_from_phonebook():
    with open('E:\Домашка\HW Python\Task38\phonebook.txt', 'r', encoding='utf-8') as f_rem:
        book = f_rem.read().splitlines()
        human = input('Введите фамилию, имя или отчество: ')
        for person in book:
            some_man = person.split(':')
            buf = some_man[0]
            if buf == human:
                book.remove(person)
            else:
                name = buf.split()
                for partname in name:
                    if partname == human:
                        book.remove(person)
        with open('E:\Домашка\HW Python\Task38\phonebook.txt', 'w', encoding='utf-8') as f_rem1:
            for person in book:
                if person == book[0]:
                    f_rem1.writelines(person)
                else:
                    f_rem1.writelines('\n')
                    f_rem1.writelines(person)

print('Добро пожаловать в телефонный справочник!')
print('Выберите режим работы со справочником:')
mode = int(input('1 - чтение, 2 - запись, 3 - изменение, 4 - удаление: '))
if mode == 1:
    Read_phonebook()
elif mode == 2:
    Entry_phonebook()
elif mode == 3:
    Change_phonebook()
elif mode == 4:
    Remove_from_phonebook()
else:
    print('Не корректный режим')
