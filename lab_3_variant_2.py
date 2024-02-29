import numpy as np

max_capacity = 10

number_of_tests = 1000

days_to_fill = []
for _ in range(number_of_tests):
    days = 0
    current_capacity = 0

    while current_capacity < max_capacity:
        incoming_packets = np.random.randint(0, 4)
        current_capacity = min(max_capacity, current_capacity + incoming_packets)
        days += 1

    days_to_fill.append(days)

# Оценка математического ожидания числа дней до полного заполнения бака
expected_days_to_fill = np.mean(days_to_fill)

print("Оценка математического ожидания числа дней до полного заполнения бака:", expected_days_to_fill)
