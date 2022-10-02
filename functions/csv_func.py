import db.db_csv as dbc
import gui.gui as gui


# Выбран тип .csv
def type_csv():
    print('Для работы выбран тип .csv')
    while True:
        match gui.get_func():
            case 'new':
                dbc.add_new_data(gui.get_lname(), 
                                    gui.get_fname(),
                                    gui.get_birth_date(),
                                    gui.get_phone_num())
            case 'new_number':
                dbc.add_new_number(gui.get_id, gui.get_phone_num)
            case 'read':
                dbc.read_csv()
            case 'del':
                dbc.del_data(gui.get_id())
            case 'find':
                dbc.find_data(gui.get_lname())
            case 'edit':
                operation = gui.get_operation()
                match operation:
                    case 'fname':
                        attribute = gui.get_fname()
                    case 'lname':
                        attribute = gui.get_lname()
                    case 'birth_date':
                        attribute = gui.get_birth_date()
                    case 'number':
                        attribute = gui.get_phone_num()            
                dbc.edit_data(operation, gui.get_id(), attribute)
            case 'exit':
                return