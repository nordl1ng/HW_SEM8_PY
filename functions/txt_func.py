import db.db_txt as dbt
import gui.gui as gui


# Выбран тип .txt
def type_txt():
    print('Для работы выбран тип .txt')
    while True:
        match gui.get_func():
            case 'new':
                dbt.add_new_data(gui.get_lname(), 
                                    gui.get_fname(),
                                    gui.get_birth_date(),
                                    gui.get_phone_num())
            case 'new_number':
                dbt.add_new_number(gui.get_id, gui.get_phone_num)
            case 'read':
                dbt.read_csv()
            case 'del':
                dbt.del_data(gui.get_id())
            case 'find':
                dbt.find_data(gui.get_lname())
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
                dbt.edit_data(operation, gui.get_id(), attribute)
            case 'exit':
                return