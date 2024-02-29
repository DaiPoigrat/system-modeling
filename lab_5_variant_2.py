import numpy as np

mu = 100
sigma = 5


# Функция для моделирования веса одной упаковки
def simulate_package_weight(mu, sigma, num_boxes_in_package):
    weight_per_box = np.random.normal(mu, sigma, num_boxes_in_package)
    return np.sum(weight_per_box)


number_of_tests = 1000

num_boxes_in_package = 10

weights = [simulate_package_weight(mu, sigma, num_boxes_in_package) for _ in range(number_of_tests)]

# Оценка математического ожидания веса одной упаковки
expected_weight = np.mean(weights)
# Оценка среднего квадратического отклонения веса одной упаковки
std_dev_weight = np.std(weights)

print(f"Оценка математического ожидания веса одной упаковки: {expected_weight} гр.")
print(f"Оценка среднего квадратического отклонения веса одной упаковки: {std_dev_weight} гр.")
