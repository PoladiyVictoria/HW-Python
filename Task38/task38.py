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


print('Добро пожаловать в телефонный справочник!')
print('Выберите режим работы со справочником:')
mode = int(input('1 - чтение, 2 - запись: '))
if mode == 1:
    Read_phonebook()
elif mode == 2:
    Entry_phonebook()
else:
    print('Не корректный режим')
