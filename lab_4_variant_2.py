import random
import matplotlib.pyplot as plt


input_array = [random.random() for _ in range(101)]

point_array = [(input_array[i], input_array[i + 1]) for i in range(100)]

point_x = []
point_y = []
for point in point_array:
    point_x.append(point[0])
    point_y.append(point[1])

# 100 tests
plt.scatter(point_x, point_y)
# 50 tests
# plt.scatter(point_x[:50], point_y[:50])
plt.show()
