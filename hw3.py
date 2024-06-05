import exchange_currency

def main():
    print("1$에 대한 오늘의 환율은? ", end="")
    exchange_rate = float(input())
    exchange_currency.set_rate(exchange_rate)
    
    print("원화로 변환할 달러화 액수는? ", end="")
    dollar_amount = float(input())
    won_amount = exchange_currency.to_won(dollar_amount)
    print(int(dollar_amount), '달러는', int(won_amount), '원입니다')
    
    print("달러화로 변환할 원화 액수는? ", end="")
    won_amount = float(input())
    dollar_amount = exchange_currency.to_dollar(won_amount)
    print(int(won_amount), '원은', dollar_amount, '달러입니다')

if __name__ == "__main__":
    main()
