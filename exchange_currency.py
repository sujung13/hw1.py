# exchange_currency.py
exchange_rate = 0

def set_rate(won):
    global exchange_rate
    exchange_rate = won

def get_rate():
    return exchange_rate

def to_dollar(won):
    return won / exchange_rate

def to_won(dollar):
    return dollar * exchange_rate

def main():
    print("### 환율 변환 모듈 테스트 ###")
    set_rate(1010)
    print("오늘의 환율", get_rate())
    won_amount = 2020
    dollar_amount = to_dollar(won_amount)
    print(won_amount, "원 =", dollar_amount, "달러")
    dollar_amount = 2
    won_amount = to_won(dollar_amount)
    print(dollar_amount, "달러 =", won_amount, "원")

if __name__ == "__main__":
    main()
