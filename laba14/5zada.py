"""Recur17. Вывести значение целочисленного выражения, заданного в виде строки S. Выражение
определяется следующим образом:
<выражение> ::= <цифра> |
(<выражение><знак><выражение>)
<знак>
::= + | − | *"""
s = input("Введите выражение: ")
def calc(s):
    # Базовый случай - строка из одной цифры
    if len(s) == 1:
        return int(s)

    # Проверка на внешние скобки и их удаление
    if s[0] == '(' and s[-1] == ')':
        # Рекурсивно проверяем, являются ли скобки внешними
        def check_outer(expr, start, end, balance):
            if start > end:
                return True
            if expr[start] == '(':
                balance += 1
            elif expr[start] == ')':
                balance -= 1
            if balance == 0 and start < end:
                return False
            return check_outer(expr, start + 1, end, balance)

        if check_outer(s, 0, len(s) - 1, 0):
            return calc(s[1:-1])

    # Поиск операций + и - (слева направо, вне скобок)
    def find_operation(expr, pos, balance):
        if pos >= len(expr):
            return -1, None

        if expr[pos] == '(':
            balance += 1
        elif expr[pos] == ')':
            balance -= 1
        elif balance == 0 and (expr[pos] == '+' or expr[pos] == '-'):
            return pos, expr[pos]

        return find_operation(expr, pos + 1, balance)

    # Поиск операции * (если нет + или -)
    def find_mult(expr, pos, balance):
        if pos >= len(expr):
            return -1, None

        if expr[pos] == '(':
            balance += 1
        elif expr[pos] == ')':
            balance -= 1
        elif balance == 0 and expr[pos] == '*':
            return pos, expr[pos]

        return find_mult(expr, pos + 1, balance)

    # Сначала ищем + или -
    pos, op = find_operation(s, 0, 0)

    if pos != -1:
        if op == '+':
            return calc(s[:pos]) + calc(s[pos + 1:])
        else:  # op == '-'
            return calc(s[:pos]) - calc(s[pos + 1:])

    # Если нет + или -, ищем *
    pos, op = find_mult(s, 0, 0)

    if pos != -1:
        return calc(s[:pos]) * calc(s[pos + 1:])

    return int(s)


result = calc(s)
print(f"Результат: {result}")