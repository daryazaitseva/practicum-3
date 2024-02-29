import math

a, b, c = map(int, input('Введите стороны треугольника ').split())
cos_a = (a**2 + c**2 - b**2)/(2*a*c)
cos_b = (a**2 + b**2 - c**2)/(2*a*b)
cos_c = (c**2 + b**2 - a**2)/(2*c*b)
angle_a = math.degrees(math.acos(cos_a))
angle_b = math.degrees(math.acos(cos_b))
angle_c = math.degrees(math.acos(cos_c))
print(angle_a, angle_b, angle_c)
