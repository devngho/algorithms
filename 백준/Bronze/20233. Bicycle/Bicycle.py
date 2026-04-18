a, x, b, y, t = [int(input()) for _ in range(5)]

a_price = max(21 * (t - 30), 0) * x + a
b_price = max(21 * (t - 45), 0) * y + b

print(a_price)
print(b_price)