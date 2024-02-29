ATT = int(input())
COMP = int(input())
YDS = int(input())
TD = int(input())
INT = int(input())
passer_rating = ((8.4 * YDS) + (330 * TD) + (100 * COMP) - (200 * INT)) / ATT
if passer_rating > 2.375:
    passer_rating = 2.375
    print(passer_rating)
elif passer_rating < 0:
    passer_rating = 0
    print(passer_rating)
else:
    print(passer_rating)