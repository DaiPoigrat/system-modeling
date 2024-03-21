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

    # print(f'{time_starting = }')
    # print(f'{time_coming = }')
    # print(f'{time_ending = }')
    # time_starting = [0., 0.93624036, 2.6661132, 3.58891513, 3.88301918,
    #                  4.37584845, 4.54287656, 5.23235487, 5.63118284, 5.77629914]
    # time_coming = [0., 0.93624036, 2.6661132, 3.58891513, 3.88301918,
    #                4.02671971, 4.54287656, 4.64180648, 5.63118284, 5.77629914]
    # time_ending = [0.07504464, 2.06506288, 2.85571002, 4.45395522, 4.37584845,
    #                5.4090168, 5.23235487, 5.55532343, 5.71287169, 5.7997083]
    print(f'{time_coming = }')
    print(f'{time_ending = }')

    # считаем u
    time_in_system = 0
    for i in range(num_requests):
        time_in_system += time_ending[i] - time_coming[i]

    serve_1 = []
    serve_2 = []
    tau_dict = {}
    for i in range(num_requests):
        print(f'-----------------------------------------------------------')
        current_task_arrive = time_coming[i]
        current_task_ending = time_ending[i]
        # print(f'{i = }, {current_task_arrive = }, {current_task_ending = }')
        # интервал на котором смотрим
        current_task_lifetime = [current_task_arrive, current_task_ending]

        # если таск ждал в 1 приборе, то он в нем же и начнет
        if current_task_arrive in serve_1:
            serve_1 = [serve_1[-1], current_task_ending]
        # если таск ждал во 2 приборе, то он в нем же и начнет
        if current_task_arrive in serve_2:
            serve_2 = [serve_2[-1], current_task_ending]

        if serve_1 and serve_1[-1] < current_task_arrive:
            serve_1 = []
        if serve_2 and serve_2[-1] < current_task_arrive:
            serve_2 = []

        # если 1 аппарат свободен
        if not serve_1:
            # print(f'ADDED 1')
            serve_1 = current_task_lifetime
        # иначе если 2 аппарат свободен
        elif not serve_2:
            # print(f'ADDED 2')
            serve_2 = current_task_lifetime

        next_task_idx = i + 1
        # print('BEFORE WHILE')
        # print(f'{serve_1 = }')
        # print(f'{serve_2 = }')
        while next_task_idx < num_requests and time_coming[next_task_idx] < current_task_ending:
            next_task_arrive = time_coming[next_task_idx]
            next_task_ending = time_ending[next_task_idx]

            next_task_lifetime = [next_task_arrive, next_task_ending]

            # print(f'{next_task_idx = }, {next_task_lifetime = }')
            # если 1 аппарат свободен
            if not serve_1:
                serve_1 = next_task_lifetime
            # иначе если 2 аппарат свободен
            elif not serve_2:
                serve_2 = next_task_lifetime
            # если оба заняты, то попадет в тот, где работа закончится раньше
            else:
                serve_1_end_time = serve_1[-1]
                serve_2_end_time = serve_2[-1]

                if serve_1_end_time < serve_2_end_time:
                    if next_task_arrive < serve_1_end_time:
                        serve_1.insert(len(serve_1) - 1, time_coming[next_task_idx])
                else:
                    if next_task_arrive < serve_2_end_time:
                        serve_2.insert(len(serve_2) - 1, time_coming[next_task_idx])

            next_task_idx += 1

        print(f'{i = }')
        print(f'{serve_1 = }')
        print(f'{serve_2 = }')
        full_timeline = serve_1.copy()
        full_timeline.extend(serve_2)
        full_timeline = sorted(full_timeline)
        print(f'Общий интервал: {full_timeline}')
        count = 0

        for i in range(len(full_timeline) - 1):
            if full_timeline[i] == serve_1[0]:
                count += 1
            elif full_timeline[i] == serve_1[-1]:
                count -= 1
            elif full_timeline[i] == serve_2[0]:
                count += 1
            elif full_timeline[i] == serve_2[-1]:
                count -= 1
            else:
                count += 1
            print(f'{count = }, [{full_timeline[i]}, {full_timeline[i + 1]}]')
            if count not in tau_dict:
                tau_dict[count] = []
            tau_dict[count].append(full_timeline[i + 1] - full_timeline[i])

    print(f'{tau_dict = }')
    ps = []
    for key in tau_dict:
        if key == 0:
            continue
        ps.append(p_k(tau_dict[key], time_ending[-1]))

    return mean(ps), time_in_system / num_requests


# Оценка мат ожидания для 1000 запросов
n, u = simulate_system(1000)

print("Математическое ожидание длительности пребывания требований в системе (u):", u)
print("Математическое ожидание числа требований в системе (nu):", n)
