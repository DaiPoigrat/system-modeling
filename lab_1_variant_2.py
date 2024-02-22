t_bread_fresh = 150
t_room = 20
t_bread_final = 40
k = 0.02
h = 0.01
time = 0

while t_bread_fresh >= t_bread_final:
    tmp_bread_t = k * (t_bread_fresh - t_room)
    t_bread_fresh -= tmp_bread_t
    time += 1

print(f'{time = } sec')
