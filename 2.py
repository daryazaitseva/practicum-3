time = int(input('Введите целое число от 1 до 86400: '))
hours = time // 3600
minutes = (time - (hours * 3600)) // 60
sec = (time - (hours * 3600)) - (minutes * 60)
print(hours, 'часов', minutes, 'минут', sec, 'секунд')