import datetime

today = input()
dday = input()

t_y, t_m, t_d = map(int, today.split())
raw_t_y, raw_t_m, raw_t_d = t_y, t_m, t_d
d_y, d_m, d_d = map(int, dday.split())

t = datetime.date(t_y, t_m, t_d)
d = datetime.date(d_y, d_m, d_d)

if (d - t).days >= 365243:
    print("gg")
else:
    print(f"D-{(d - t).days}")
