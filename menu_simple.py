from menu_template import start_menu
# Итерация 1: Заглушки

def menu_f1():
    print('--> Вызвана функция f1 (заглушка)')
    
def menu_f2():
    print('--> Вызвана функция f2 (заглушка)')

def menu_g1():
    print('--> Вызвана функция g1 (заглушка)')
    
def menu_g2():
    print('--> Вызвана функция g2 (заглушка)')

def menu_sub1():
    """Подменю 1: Однократное действие и возврат"""
    print('*** Вызвано menu_sub1 (заглушка) ***')
    # Здесь должен быть код для вызова f1 или f2
    
def menu_sub2():
    """Подменю 2: Циклическое действие"""
    print('*** Вызвано menu_sub2 (заглушка) ***')
    # Здесь должен быть код для вызова g1 или g2
    
def menu_main():
    """Главное меню"""
    print('--- Запуск menu_main (заглушка) ---')
    # Здесь должен быть цикл для вызова sub1 или sub2
    start_menu('Main menu input prompt', 'Error prompt', {}) # Имитация вызова
    
# Точка входа
if __name__ == "__main__":
    from menu_template import start_menu # Пока что это не сработает, но готовимся
    menu_main()
    print('--- Выход из программы ---')