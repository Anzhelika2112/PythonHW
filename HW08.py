# Задача 38: Дополнить телефонный справочник возможностью изменения 
# и удаления данных. Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных

def write_name():
    name = input('Введите имя: ')
    return name


def write_surname():
    surname = input('Введите фамилию: ')
    return surname


def write_phone():
    phone = input('Введите телефон: ')
    return phone


def write_adress():
    adress = input('Введите адрес: ')
    return adress

def input_data(): # Функция добавления данных и создания текстового файла
    name = write_name()
    surname = write_surname()
    phone = write_phone()
    adress = write_adress()
    with open('phonebook.txt', 'a', encoding='utf-8') as data:
        data.write(f'{name} {surname}: {phone} {adress}\n\n')


def edit_contact():  # Функция редактирования информации в файле
    phone_book = []
    with open('phonebook.txt', 'r', encoding='utf-8') as data1:
        data = sorted(data1.readlines())
        print(data)

        index_edit_contact = int(input('Введите номер строки для редактирования: '))
        print(data[index_edit_contact - 1].rstrip().split(","))
        if index_edit_contact != 0:
            new_name = input('Введите новое имя: ')
            new_surname = input('Введите новую фамилию: ')
            new_phone = input('Введите новый телефон: ')
            new_adress = input('Введите новый адрес: ')
            data[index_edit_contact - 1] = (new_name + " " + new_surname + ", " + new_phone + ", " + new_adress + "\n")
            with open('phonebook.txt', 'w', encoding='utf-8') as data1:
                data1.write(''.join(data))
        else:
            return



def delete_contact():  # Функция удаления контакта из файла
    with open('phonebook.txt', "r+", encoding='utf-8') as data1:
        data = sorted(data1.readlines())
        print(data)

        index_edit_contact = int(input('Введите номер строки для удаления: '))
        if index_edit_contact != 0:
            data.pop(index_edit_contact - 1)
            with open('phonebook.txt', "w", encoding='utf-8') as data1:
                data1.write(''.join(data))

        else:
            return
        
# input_data() # Функция добавления данных и создания текстового файла

edit_contact() # Функция редактирования информации в файле

delete_contact() # Функция удаления контакта из файла