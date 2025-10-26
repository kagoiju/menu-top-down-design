# Итерация 2: Полная реализация

def is_int(s):
    """Проверка на то, что s - целое число"""
    try:
        if type(s) is int:
            return True
        if s is None:
            return False
        if not s.isdecimal():
            return False
        int(s)
        return True
    except (Exception, ValueError, TypeError):
        return False

def entering_valid_value_integer(message_input: str, message_err: str, template: list):
    """Ввод допустимого целого числа"""
    while True:
        ch = input(message_input, )
        if is_int(ch):
            ch = int(ch)
            if ch in template:
                return ch
        print(message_err)

def start_menu(message_input: str, message_err: str, template: dict):
    """Универсальное меню. Выбор пункта меню вводом его номера."""
    while True:
        # Ввод корректного ch
        ch = entering_valid_value_integer(message_input,
                                          message_err,
                                          list(template))
        # Выбор действия
        f, is_break = template[ch]
        f()
        if is_break:
            break
    return False