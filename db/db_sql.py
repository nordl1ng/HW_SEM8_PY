import sqlite3 as sql

handbook = sql.connect(r'db\handbook.db')
cur = handbook.cursor()

# Подключение к БД:
def init():
    handbook.execute("""CREATE TABLE IF NOT EXISTS people(
        people_id INTEGER PRIMARY KEY AUTOINCREMENT,
        fname TEXT,
        lname TEXT,
        birth_date TEXT);
        """)

    handbook.execute("""CREATE TABLE IF NOT EXISTS phone_number(
        number_id INTEGER PRIMARY KEY AUTOINCREMENT,
        number INTEGER,
        people_id INTEGER,
        FOREIGN KEY(people_id) REFERENCES people(people_id));
        """)
    handbook.commit()

# Добавление записи:
def add_new_data(lname, fname, birth_date, number):
    try:
        cur.execute("INSERT INTO people VALUES(NULL, ?, ?, ?);", (lname, fname, birth_date))    
        id = cur.execute("SELECT people_id FROM people").fetchall()
        id = id[len(id)-1][0]
        cur.execute("INSERT INTO phone_number VALUES(NULL, ?, ?);", (number, id))
        handbook.commit()
        print('Запись успешно добавлена!')
    except sql.Error as error:
        print("Ошибка при работе с SQLite", error)

# Новый номер:
def add_new_number(data, id):
    try:
        cur.execute("INSERT INTO phone_number VALUES(NULL, ?, ?)", (data, id))    
        handbook.commit()
        print('Номер успешно добавлен!')
    except sql.Error as error:
        print("Ошибка при работе с SQLite", error)

# Считывание базы данных:
def read_base():  
    try:  
        result_list = cur.execute("""SELECT people.people_id, fname, lname, phone_number.number 
                                FROM people LEFT JOIN phone_number 
                                ON phone_number.people_id=people.people_id;""").fetchall()
        print(result_list)
        print('Считывание завершено!')
    except sql.Error as error:
        print("Ошибка при работе с SQLite", error)

# Удаление записи из базы данных:
def del_data(id):
    try:
        cur.execute("DELETE FROM people WHERE people_id = ?;", (id,))
        cur.execute("DELETE FROM phone_number WHERE people_id = ?;", (id,))
        handbook.commit()
        print('Запись успешно удалена!')
    except sql.Error as error:
        print("Ошибка при работе с SQLite", error)

# Поиск записей:
def find_data(data):    
    try:
        result = cur.execute("SELECT * FROM people WHERE lname == ?;", (data,)).fetchall()
        print('Найдено:')
        print(result)
        print('Поиск завершен!')
    except sql.Error as error:
        print("Ошибка при работе с SQLite", error)

# Редактирование записи:
def edit_data(operation, id, data):
    try:
        match operation:
            case 'number':
                cur.execute("UPDATE phone_number SET number = ? WHERE people_id == ?", (data, id))    
            case 'lname':
                cur.execute("UPDATE people SET lname = ? WHERE people_id == ?", (data, id))
            case 'fname':
                cur.execute("UPDATE people SET fname = ? WHERE people_id == ?", (data, id))
            case 'birth_date':
                cur.execute("UPDATE people SET birth_date = ? WHERE people_id == ?", (data, id))           
        handbook.commit()
        print('Запись успешно отредактирована!')
    except sql.Error as error:
        print("Ошибка при работе с SQLite", error)

# Завершение работы с бд:
def close():
    handbook.close()