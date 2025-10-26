# menu_simple.py - Итерация 3: Полная реализация логики меню

from menu_template import start_menu
import sys # Импорт для exit(0)

# --- Функции действий (f1, f2, g1, g2) ---

def menu_f1():
    print('*** Вычисление: f1(x) ***')
    input("Нажмите Enter, чтобы продолжить...", )

def menu_f2():
    print('*** Вычисление: f2(x) ***')
    input("Нажмите Enter, чтобы продолжить...", )

def menu_g1():
    print('*** Вычисление: g1(x) ***')
    input("Нажмите Enter, чтобы продолжить...", )

def menu_g2():
    print('*** Вычисление: g2(x) ***')
    input("Нажмите Enter, чтобы продолжить...", )

# --- Подменю ---

def menu_sub1():
    """
    Однократное выполнение действия и возврат в главное меню (is_break=True).
    """
    caption_start = "=== menu_sub1 === \n 1) f1(x) \n 2) f2(x) \n 0) return \n"
    caption_err = 'Ошибка ввода. Попробуйте снова.'
    menu_template = {
        0: (lambda: print("Возврат в главное меню..."), True), # is_break=True -> выход
        1: (menu_f1, True),   # is_break=True -> выход после выполнения
        2: (menu_f2, True)}   # is_break=True -> выход после выполнения
        
    start_menu(caption_start, caption_err, menu_template)


def menu_sub2():
    """
    Циклическое. Возврат в главное меню только через пункт 0 (is_break=False).
    """
    caption_start = "=== menu_sub2 === \n 1) g1(x) \n 2) g2(x) \n 0) return \n"
    caption_err = 'Ошибка ввода. Попробуйте снова.'
    menu_template = {
        0: (lambda: print("Возврат в главное меню..."), True), # is_break=True -> выход
        1: (menu_g1, False),  # is_break=False -> остаемся в меню
        2: (menu_g2, False)}  # is_break=False -> остаемся в меню
    
    start_menu(caption_start, caption_err, menu_template)

# --- Главное меню ---

def menu_main():
    """
    Циклическое. Выход из меню только через пункт 0.
    """
    caption_start = "=== menu_main === \n 1) menu_sub1 \n 2) menu_sub2 \n 0) exit \n"
    caption_err = 'Ошибка ввода. Попробуйте снова.'
    menu_template = {
        0: (lambda: print("Завершение программы."), True), # is_break=True -> выход
        1: (menu_sub1, False), # is_break=False -> остаемся в меню
        2: (menu_sub2, False)} # is_break=False -> остаемся в меню
        
    start_menu(caption_start, caption_err, menu_template)

# --- Точка входа ---

if __name__ == "__main__":
    menu_main()
    sys.exit(0)