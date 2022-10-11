n = int(input("Введите первое число\n"))
m = int(input("Введите второе"
              " число\n"))
while (n != m):
    if (n > m):
        n -= m
    else:
        m -= n
print(n);