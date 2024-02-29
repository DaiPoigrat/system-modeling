import matplotlib.pyplot as plt

a_min = -0.2
a_max = 0

a = -0.1

h = 0.01

plt.figure()

while a_min < a_max:
    x_0 = -9
    y_0 = 9

    x_values = [x_0]
    y_values = [y_0]

    a = a_min

    for i in range(50):
        current_x = x_0
        current_y = y_0

        new_x = a * current_x - current_y
        new_y = current_x + a * current_y

        x_0 = new_x
        y_0 = new_y

        x_values.append(new_x)
        y_values.append(new_y)

    plt.plot(x_values, y_values)

    a_min += h


plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
