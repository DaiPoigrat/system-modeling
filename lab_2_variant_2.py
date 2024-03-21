import matplotlib.pyplot as plt

a_min = -0.2
a_max = 0

# начальное значение а
a = -0.1
# шаг приращения а
h = .1

plt.figure()

while a_min < a_max:
    # стартовые значения координат (взято от балды)
    x_0 = -1
    y_0 = 1

    x_values = []
    y_values = []

    a = a_min

    for i in range(100):
        current_x = x_0
        current_y = y_0
        # dx/dt = ax - y
        new_x = current_x + h * (a * current_x - current_y)
        # dy/dt = x + ay
        new_y = current_y + h * (current_x + a * current_y)

        x_0 = new_x
        y_0 = new_y

        x_values.append(new_x)
        y_values.append(new_y)

    plt.plot(x_values, y_values)
    print(x_values)
    print(y_values)
    a_min += h


plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
