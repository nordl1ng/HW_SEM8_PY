import db.db_sql as dbs
import gui.gui as gui


# Выбран тип .db
def type_sql():
    print('Для работы выбран тип .db')
    dbs.init()
    while True:
        match gui.get_func():
            case 'new':
                dbs.add_new_data(gui.get_lname(), 
                                    gui.get_fname(),
                                    gui.get_birth_date(),
                                    gui.get_phone_num())                
            case 'new_number':
                dbs.add_new_number(gui.get_phone_num(), gui.get_id())                
            case 'read':
                dbs.read_base()                
            case 'del':
                dbs.del_data(gui.get_id())                
            case 'find':
                dbs.find_data(gui.get_lname())                
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
                dbs.edit_data(operation, gui.get_id(), attribute)
            case 'exit':
                dbs.close()
                return