"""
Условие
M|M|2|inf|inf
- Пуассоновский поток требований
- одинаково экспоненциально распределенные длительности обслуживания на каждом приборе
- 2 обслуживающих прибора
- бесконечная очередь
- бесконечное число источников требований
"""

import numpy as np

# сколько требований поступает в единицу времени
LAMBDA = 1
# сколько требований обслуживает 1 прибор
MU = 2


def exponential_generation(scale: float, num_requests: int):
    result = []
    for i in range(num_requests):
        result.append(-np.log(np.random.random()) / scale)
    return result


def p_k(taus, T):
    return sum(taus) / T


def mean(ps):
    summa = 0
    for i in range(1, len(ps)):
        summa += i * ps[i]

    return summa


# Имитационная модель
def simulate_system(num_requests):
    # времена между прибытиями требований
    time_between_arrivals = exponential_generation(scale=LAMBDA, num_requests=num_requests)
    # времена выполнения требований
    service_time = exponential_generation(scale=MU, num_requests=num_requests)

    # время поступления
    time_coming = np.zeros(num_requests)
    # время начала выполнения
    time_starting = np.zeros(num_requests)
    # время окончания выполнения
    time_ending = np.zeros(num_requests)

    # параметры первых 2 требований
    time_ending[0] = service_time[0]
    time_coming[1] = time_between_arrivals[0]
    time_starting[1] = time_between_arrivals[0]
    time_ending[1] = time_between_arrivals[0] + service_time[1]

    for i in range(2, num_requests):
        time_coming[i] = time_between_arrivals[i - 1] + time_coming[i - 1]

        time_starting[i] = max(min(time_ending[i - 1], time_ending[i - 2]), time_coming[i])

        time_ending[i] = time_starting[i] + service_time[i]

    print(f'{time_coming = }')
    print(f'{time_starting = }')
    print(f'{time_ending = }')

    # считаем u
    time_in_system = 0
    for i in range(num_requests):
        time_in_system += time_ending[i] - time_coming[i]

    serve_1 = []
    serve_2 = []
    for i in range(num_requests):
        current_task_arrive = time_coming[i]
        current_task_ending = time_ending[i]
        current_task_lifetime = [current_task_arrive, current_task_ending]

        if not serve_1:
            serve_1 = current_task_lifetime
        elif not serve_2:
            serve_2 = current_task_lifetime
        else:
            serve_1_end_time = serve_1[-1]
            serve_2_end_time = serve_2[-1]

            if serve_1_end_time < serve_2_end_time:
                serve_1.insert(len(serve_1) - 1, current_task_arrive)
            else:
                serve_2.insert(len(serve_1) - 1, current_task_arrive)



    return 0, time_in_system / num_requests


# Оценка мат ожидания для 1000 запросов
n, u = simulate_system(10)

print(f'{u = }')
