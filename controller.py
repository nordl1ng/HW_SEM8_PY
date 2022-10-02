import functions.general_func as generalf
import functions.txt_func as txtf
import functions.csv_func as csvf
import functions.sql_func as sqlf

def button_click():
    while True:
        match generalf.choose_type():
            case '.db':
                sqlf.type_sql()
            case '.txt':
                txtf.type_txt()
            case '.csv':
                csvf.type_csv()
            case 'exit':
                return