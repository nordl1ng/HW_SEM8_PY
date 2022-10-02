path = (r'db\handbook.txt')

# Добавление записи:
def add_new_data(lname, fname, birth_date, number):
    temp = lname + '; ' + fname + '; ' + birth_date + '; ' + number
    
    with open(path, 'r', encoding='utf-8', newline='\n') as file:     
        data_for_id = file.readlines()
    data_for_id = [data_for_id[i].split('; ') for i in range(len(data_for_id))]
    data_for_id = [data_for_id[i][0] for i in range(len(data_for_id))]

    new_id = max(tuple(map(int, data_for_id))) + 1
    
    temp = str(new_id)  + '; ' + temp

    with open(path, 'a', encoding='utf-8') as file:
        file.write(f'{temp}\n')    
    print('Запись успешно добавлена')

# Новый номер:
def add_new_number(id, number):
    with open(path, 'r', encoding='utf-8', newline='\n') as file:     
        data = file.readlines()
    data = [data[i].split('; ') for i in range(len(data))]
    for i in range(len(data)):
        if data[i][0] == id: data[i].append(number)

    data = ['; '.join(data[i]) for i in range(len(data))]
    with open(path, 'w', encoding='utf-8') as file:
        file.write(f'{data}\n')   
    print('Номер успешно добавлен') 

# Считывание базы данных:
def read_csv():
    with open(path, 'r', encoding='utf-8') as file:     
        data = file.readlines()
        for row in data:
            print(row, end='')
    print('Считывание завершено')

# Удаление записи из базы данных:
def del_data(id):
    with open(path, 'r', encoding='utf-8') as file:     
        data = file.readlines()
    data = [data[i].split('; ') for i in range(len(data))]
    data = ['; '.join(data[i]) for i in range(len(data)) if data[i][0] != id]

    with open(path, 'w', encoding='utf-8') as file:
        for row in data:
            file.write(f'{row}')
    print('Запись успешно удалена')

# Поиск записей:
def find_data(lname):
    with open(path, 'r', encoding='utf-8') as file:     
        data = file.readlines()
    head = data[0][0:-1]
    data = [data[i][0:-1].split('; ') for i in range(len(data))]
    data = [data[i] for i in range(len(data)) if data[i][1] == lname]
    data = ['; '.join(data[i]) for i in range(len(data))]    
    print('Найдены совпадения: ')
    print(head)
    print(''.join(data))

# Редактирование записи:
def edit_data(operation, id, data):
    with open(path, 'r', encoding='utf-8') as file:     
        temp_data = file.readlines()
    temp_data = [temp_data[i][0:-1].split('; ') for i in range(len(temp_data))]

    for i in range(len(temp_data)):
        if temp_data[i][0] == id:
            match operation:                    
                    case 'lname':
                        temp_data[i][1] = data
                    case 'fname':
                        temp_data[i][2] = data
                    case 'birth_date':
                        temp_data[i][3] = data
                    case 'number':
                        temp_data[i][4] = data
    
    temp_data = ['; '.join(temp_data[i]) for i in range(len(temp_data))]

    with open(path, 'w', encoding='utf-8') as file:
        for row in temp_data:
            file.write(f'{row}\n')
    print('Запись успешно отредактирована')