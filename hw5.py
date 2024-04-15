def read_single_digit(x):
    if x == 1:
        return '일'
    elif x == 2:
        return '이'
    elif x == 3:
        return '삼'
    elif x == 4:
        return '사'
    elif x == 5:
        return '오'
    elif x == 6:
        return '육'
    elif x == 7:
        return '칠'
    elif x == 8:
        return '팔'
    elif x == 9:
        return '구'
    else:
        return '영'

def read_number(num):
    res1 = read_single_digit(num // 100)
    res2 = read_single_digit((num // 10) % 10)
    res3 = read_single_digit(num % 10)
    return res1, res2, res3

# 주 프로그램부
num = int(input("세 자리 정수 입력: "))
if 0 <= num < 10:
    res1 = read_single_digit(num)
    print(res1)
elif 100 <= num < 1000:
    res1, res2, res3 = read_number(num)
    print(res1, res2, res3)
else:
    res1 = read_single_digit(num // 10)
    res2 = read_single_digit(num % 10)
    print(res1, res2)
