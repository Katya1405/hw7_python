import datetime


def log_exp (surname):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'Запрос по фамилии {surname} осуществлен в {datetime.datetime.now()} \n')

def log_imp(info):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'Данные человека {info} успешно записаны в справочник в {datetime.datetime.now()} \n')