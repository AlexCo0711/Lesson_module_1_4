# Практическая работа по уроку "Организация программ и методы строк".
# вариант 1 используя функцию len()
my_string = input('Введите слово или текст: ')
print('Количество символов в тексте включая пробелы:', len(my_string))

# вариант 2, через организацию цикла
my_string = input('Введите слово или текст: ')


def symbol(my_string):
    prohod = 0
    for i in my_string:
        prohod = prohod + 1
    return prohod


print('Количество символов в тексте включая пробелы:', symbol(my_string))

# task 2
print(my_string.upper())
print(my_string.lower())
print(my_string.replace(" ", ""))
print(my_string[0])
print(my_string[-1])
