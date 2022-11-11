""" Компьютер угадывает число менее чем за 20 попыток """
import numpy as np
number = np.random.randint(1,101) # загадываем число 

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)
print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int:
    """За какое количество попытом в среднем из 1000 подходов угадывает наш алгоритм 

    Args:
        random_predict ([type]): функция угадывания 

    Returns:
        int: среднее количество попыток 
    """
    count = 0
    mn = 1
    mx = 100
    
    # number = np.random.randint(1, 101)
    
    while True:
        count += 1
        md = round((mn + mx)/2) # считаем среднюю (половину числового ряда)
        print(md)
        if md > number:
            mx = md
        elif md < number:
            mn = md
        else:
            print(f'Компьютер угадал загаданное число за {count} попыток. Это число {number}')
            break # конец игры и выход из цикла
        
    return(count)

# RUN
if __name__ == '__main__':
    score_game(random_predict)

