"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number > predict_number*2:
            count+=1
            predict_number in range(predict_number*2, 101)
        elif number > predict_number +5:
            count+=1
            predict_number in range(predict_number+5, 101)
        else:
            count+=1
            break  # выход из цикла если угадали
    return count