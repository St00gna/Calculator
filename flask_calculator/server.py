import re
from typing import Union




    # Функція для обчислення виразів без дужок
def evaluate(expression: str) -> Union[int, float, str]:

        # Розділяємо по операціям
    values = re.findall(r'\d+(?:\.\d+)?|[-+*/]', expression)

        # Превіряємо чи довший за 2 елементи, якщо так, то переводимо у числові дані та обчислюємо, а якщо ні повертаємо значення
    if len(values) >= 3:
        for i in range(len(values)):
            is_num = bool(re.match(r'^-?\d+(\.\d+)?$', values[i]))
            if is_num:
                if '.' in values[i]:
                    values[i] = float(values[i])
                else:
                    values[i] = int(values[i])

        if values[0] == '-':
            values.pop(0)
            for i in range(len(values)):
                if values[i] == '+':
                    values[i] = '-'
                elif values[i] == '-':
                    values[i] = '+'

            # Виконуємо операції в порядку їх пріорітету
        try:
            while '*' in values or '/' in values:
                for i in range(len(values)):
                    if values[i] == '*':
                        values[i-1] = values[i-1] * values[i+1]
                        del values[i:i+2]
                        break
                    elif values[i] == '/':
                        values[i-1] = values[i-1] / values[i+1]
                        del values[i:i+2]
                        break

                # Виконуємо операції додавання та віднімання
            result = values[0]
            for i in range(1, len(values), 2):
                if values[i] == '+':
                    result = result + values[i+1]
                elif values[i] == '-':
                    result = result - values[i+1]
        except:
            return 'Value Error. Invalid expression'

        if expression[0] == '-':
            if str(result)[0] == '-':
                result = str(result)[1:]
            else:
                result = '-' + str(result)

    else:
        result = expression



        # Переводимо результат у числовий формат
    if '.' in str(result) and str(result)[-1] == '0':
        return int(float(result))
    elif '.' not in str(result):
        return int(result)
    else:
        return float(result)


def check_result(result_from_parentheses: Union[int, str], open_index: int, close_index:int, expression:str) -> Union[int, str]:
    new_expression = ''
    if result_from_parentheses >= 0:
        new_expression = expression[:open_index] + str(result_from_parentheses) + expression[close_index + 1:]

    elif result_from_parentheses < 0 and expression[open_index - 1] == '-':
        new_expression = expression[:open_index - 1] + '+' + str(result_from_parentheses)[1:] + expression[close_index + 1:]

    elif result_from_parentheses < 0:
        if expression[open_index - 1] == '*' or expression[open_index - 1] == '/':
            string = expression[:open_index]
            for i in range(len(string) - 1, -1, -1):
                if string[i] == '+':
                    new_expression = expression[:i] + '-' + expression[i + 1:open_index] + str(result_from_parentheses)[1:] + expression[close_index + 1:]
                    break
                elif string[i] == '-':
                    new_expression = expression[:i] + '+' + expression[i + 1:open_index] + str(result_from_parentheses)[1:] + expression[close_index + 1:]
                    break
                elif string[i] == '(':
                    if string[i + 1] == '-':
                        new_expression = expression[:i + 1] + '' + expression[i + 1:open_index] + str(result_from_parentheses)[1:] + expression[close_index + 1:]
                        break
                    else:
                        new_expression = expression[:i + 1] + '-' + expression[i + 1:open_index] + str(result_from_parentheses)[1:] + expression[close_index + 1:]
                        break

        if expression[open_index - 1] == '+':
                new_expression = expression[:open_index - 1] + str(result_from_parentheses) + expression[close_index + 1:]

    return new_expression


    # Функція для обробки дужок та обчислення виразів у них
def calculator(expression: str) -> Union[int, float, str]:
        # Знаходимо першу закриваючу дужку
    close_index = expression.find(')')

        # Знаходимо останню відкриваючу дужку перед закриваючою
    open_index = expression.rfind('(', 0, close_index)

    if close_index == -1 and open_index == -1:
            # Якщо немає закриваючої дужки, обчислюємо весь вираз
        return evaluate(expression)

    elif close_index == -1 or open_index == -1:
        return 'Value Error. Invalid expression'


        # Обчислюємо вираз у дужках та замінюємо його на результат
    sub_expression = expression[open_index + 1:close_index]
    result_from_parentheses = evaluate(sub_expression)

    new_expression = check_result(result_from_parentheses, open_index, close_index, expression)
        # Рекурсивно обробляємо решту виразу
    return calculator(new_expression)

    # Обробляємо вирази у дужках та повертаємо результат

