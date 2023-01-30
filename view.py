
def enter_for_export():
    surname = input('Введите фамилию человека, чьи данные вы хотите найти: ')
    return surname


def enter_for_import():
    print('Необходимо ввести информацию для записи данных в справочник')
    surname = input('Введите фамилию человека: ')
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    type = input('Введите тип номера (личный, домашний, рабочий): ')
    return('', surname, name, phone, type)

def print_info_export(some_info):
    print('Найдена информация по вашему запросу!')
    for i in range(len(some_info)):
        print(some_info[i])


def print_info_import():
    return('Данные успешно записаны в справочник!')