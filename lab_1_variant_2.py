import matplotlib.pyplot as plt

t_bread_fresh = 150
t_room = 20
t_bread_final = 40
k = 0.02
h = 1
time = 0

t_value_list = [0]
x_t_value_list = [t_bread_fresh]

while t_bread_fresh >= t_bread_final:
    tmp_bread_t = k * (t_bread_fresh - t_room)
    t_bread_fresh -= tmp_bread_t
    time += h

    t_value_list.append(time)
    x_t_value_list.append(t_bread_fresh)

print(f'{time = } sec')

plt.plot(t_value_list, x_t_value_list)
plt.grid(True)
plt.xlabel('Время')
plt.ylabel('Температура от времени')
plt.show()
