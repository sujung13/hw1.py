def buy(d):
  print('[구입]')
  n = input('상품명? ')
  if n in d:
    return False
  elif not n:
    return False
  else:
    cnt = int(input('수량은? '))
    d[n] = cnt
    print(f'장바구니에 {n} {cnt}개가 담겼습니다.')
    print()

def show(d):
  print('>>> 장바구니 보기:', d)
  print()

def find(d):
  print('[검색]')
  n = input('장바구니에서 확인하고자 하는 상품은? ')
  if n in d:
    print(f'{n} (는) {d[n]}개 담겨 있습니다.')
  else:
    print(f'장바구니에 {n}은(는) 없습니다.')

# 주 프로그램부
shopping_bag = {}
while True:
  if buy(shopping_bag) == False:
    break
show(shopping_bag)
find(shopping_bag)