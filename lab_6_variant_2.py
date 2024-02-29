import numpy as np


# Функция для моделирования времени до отказа элемента
def simulate_time_to_failure():
    return np.random.exponential(1)


# Функция для проверки обнаружения неисправности при техническом обслуживании
def check_maintenance():
    return np.random.choice([0, 1], p=[0.3, 0.7])


number_of_tests = 1000
fault_not_detected = 0

for _ in range(number_of_tests):
    time_to_failure = simulate_time_to_failure()
    for _ in range(int(time_to_failure / 0.5)):
        if check_maintenance() == 1:
            fault_not_detected += 1
            break

probability = fault_not_detected / number_of_tests
print(f"Вероятность того, что неисправность элемента не будет обнаружена при техническом обслуживании и элемент выйдет из строя: {probability}")
