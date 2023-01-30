
def func_export(surname):
    with open('text.txt', 'r', encoding='utf-8') as file:
        some_result_list = []
        while True:
            line = file.readline()
            if not line:
                if not file.readline():
                    break
            if line.rstrip() == surname:
                some_result_list.append(surname)
                for _ in range(3):
                    some_result_list.append(file.readline().rstrip())
    if len(some_result_list) > 0:
        return some_result_list
    else:
        return 'Такой фамилии нет в списке'


def func_import(information):
    with open('text.txt', 'a', encoding='utf-8') as info:
        for element in information:
            info.write('\n')
            info.write(element)
