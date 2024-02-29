n = int(input())
hours = n // 30
minutes = (n - hours * 30) / 0.5
print(f'С начала суток прошло {hours} часов и {minutes} минут')