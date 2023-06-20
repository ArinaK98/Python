phone_book = []
path = 'phones.txt'

def open_file():
    with open(path, 'r', encoding='utf-8') as file:
        data = file.readlines
    print(data)




# def write_contacts(phonebook):
#     with open(phonebook, 'a', encoding='utf-8') as file:
#         file.write('\n' + input(f'введите фамилию, имя, отчество и номер телефона: '))
#     return file

# def read_contacts(phonebook):
#     contacts = []
#     with open(phonebook, 'r') as file:
#         for line in file:
#             name, surname, patronymic, phone = line.strip().split()
#             contact = {
#                 'name': name,
#                 'surname': surname,
#                 'patronymic': patronymic,
#                 'phone': phone
#             }
#             print(name, surname, patronymic, phone)
#             contacts.append(contact)
#     return contacts
