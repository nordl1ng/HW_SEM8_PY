# from logging import root
# from tkinter import *
# from tkinter import ttk 

# root = Tk()
# root.title("Выберите тип файла:")
# root.geometry('450x50')  
# root.resizable(False, False)

# def r1():
#     global btn_r1
#     r1 = btn_r1['text']
#     root.destroy()
#     return r1

# def r2():
#     global btn_r2
#     r2 = btn_r2['text']
#     root.destroy()
#     return r2

# def r3():
#     global btn_r3
#     r1 = btn_r3['text']
#     root.destroy()
#     return r3

# btn_r1 = Button(root, text=".txt", width=20, height=3, command=r1)
# btn_r2 = Button(root, text=".db", width=20, height=3, command = r2)
# btn_r3 = Button(root, text=".csv", width=20, height=3, command = r3)

def get_fname():
    return input('first name = ')

def get_lname():
    return input('last name = ')

def get_birth_date():
    return input('birth date = ')

def get_phone_num():
    return input('phone number = ')

def get_id():    
    return input('id = ')

def get_func():
    return input('operation (new, new_number, read, del, find, edit, exit) = ')

def get_operation():
    return input('operation (fname, lname, birth_date, number) = ')



# def start_window():
#     btn_r1.grid(column=0, row=6)
#     btn_r2.grid(column=1, row=6) 
#     btn_r3.grid(column=2, row=6)
#     root.mainloop()




# window = Tk()  
# window.title("Телефонный справочник")
# window.geometry('400x250')  


# tab_control = ttk.Notebook(window)  
# tab1 = ttk.Frame(tab_control)  
# tab2 = ttk.Frame(tab_control)  
# tab_control.add(tab1, text='Внести изменения в справочник')  
# tab_control.add(tab2, text='Просмотр всего списка контактов')   
# tab_control.pack(expand=1, fill='both')  

# btn = Button(tab1, text="Сохранить")  
# btn.grid(column=0, row=6) 
# btn_1 = Button(tab1, text="Изменить")  
# btn_1.grid(column=1, row=6) 
# btn_2 = Button(tab1, text="Удалить")  
# btn_2.grid(column=2, row=6) 
# family = Label(tab1, text="Фамилия:")
# family.grid(column=0, row=1)  
# txt_f = Entry(tab1,width=15)  
# txt_f.grid(column=1, row=1)    
# name = Label(tab1, text="Имя:")
# name.grid(column=0, row=2)  
# txt_n = Entry(tab1,width=15)  
# txt_n.grid(column=1, row=2)
# dat = Label(tab1, text="Дата рождения:")
# dat.grid(column=0, row=3)  
# txt_dat = Entry(tab1,width=15)  
# txt_dat.grid(column=1, row=3)     
# num = Label(tab1, text="Телефон:")
# num.grid(column=0, row=4)  
# txt_num = Entry(tab1,width=15)  
# txt_num.grid(column=1, row=4) 

# window.mainloop()