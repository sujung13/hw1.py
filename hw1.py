def get_circle_area(p):
    r = int(input(p))
    w = 3.14*r*r
    return w

circle_area = get_circle_area('넓이를 구하고자 하는 원의 반지름은? ')
print('원의 넓이는?', circle_area)
