import view
import mod
import process
import logging 

def button_click():
    operation = process.choose()
    if operation == 'Экспорт':
        surname = view.enter_for_export()
        some_list = mod.func_export(surname)
        view.print_info_export(some_list)
        logging.log_exp(surname)
    else:
        info_about_someone = view.enter_for_import()
        mod.func_import(info_about_someone)
        view.print_info_import()
        logging.log_imp(info_about_someone)
