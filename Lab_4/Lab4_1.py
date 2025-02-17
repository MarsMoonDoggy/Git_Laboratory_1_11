from get_datetime import get_datetime

get_datetime()

# Импортируем класс datetime из модуля datetime для работы с датами и временем.
from datetime import datetime
# Импортируем функцию sqrt из модуля math для вычисления квадратного корня.
from math import sqrt


def main(**kwargs):
    """
    Вычисляет и выводит длину гипотенузы для пар значений, переданных в виде именованных аргументов.

    Каждый аргумент должен быть списком из двух элементов, представляющих катеты прямоугольного треугольника.
    Функция печатает длину гипотенузы для каждой пары.

    Параметры:
        **kwargs (dict): Словарь, ключи которого - имена аргументов, а значения - списки из двух чисел [a, b].

    Возвращает:
        None. Результаты выводятся на экран.

    Примеры использования:
        main(one=[10, 3], two=[5, 4])
    """
    # Цикл перебора элементов словаря kwargs. Переменная key получает пары (ключ, значение).
    for key in kwargs.items():
        # Вычисление гипотенузы по теореме Пифагора для пары чисел, указанных в списке значения.
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2)
        # Вывод результата вычисления на экран.
        print(result)


# Проверка, что данный скрипт выполняется как основная программа.
if __name__ == '__main__':
    # Фиксация времени начала выполнения программы.
    start_time = datetime.now()
    # Вызов функции main с передачей именованных аргументов в виде списков с двумя числами.
    main(
        one=[10, 3],
        two=[5, 4],
        three=[15, 13],
        four=[93, 53],
        five=[133, 15]
    )
    # Вычисление времени, затраченного на выполнение программы.
    time_costs = datetime.now() - start_time
    # Вывод на экран затраченного времени в форматированном виде.
    print(f"Время выполнения программы - {time_costs}")
