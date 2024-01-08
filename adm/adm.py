def print_menu(menu):
    for i in range(1, len(menu)+1):
        print(str(i) + '.', menu[i-1])

def ask_menu_int(tip, menu):
    print(tip)
    print_menu(menu)
    
    value = int(input('> '))
    while (value < 0 or value > len(menu)):
        print('Нет такого пункта в меню')
        value = int(input('> '))

    return value

def add_class():
    pass

def add(subject):
    funcs = []
    
def change(subject):
    pass
    
def delete(subject):
    pass
    
def query(subject):
    pass

def make(action, subject):
    funcs = [add, change, delete, query]
    funcs[action - 1](subject)

menu_level_1 = ['Добавить', 'Изменить', 'Удалить', 'Сделать запрос']
menu_level_2 = ['Класс объектов', 'Объект', 'Характеристика', 'Параметр', 'Потенциальное значение']

def main():
    print('Добро пожаловать в скрипт для администрирования БД ИКИО')
    
    action = ask_menu_int('Выберите действие', menu_level_1)
    
    subject = '' # Предмет
    if (action != 4):
        subject = ask_menu_int('Выберите предмет', menu_level_2)
    
    make(action, subject)
    
main()