def rep_char(c, n):
    print(c * n)

def welcome_message(name):
    msg1 = 'Hello ' + name
    msg2 = 'Welcome to Seoul.'
    if len(msg1) > len(msg2):
        nstr = len(msg1)
    else:
        nstr = len(msg2)
    rep_char('-', nstr * 2)
    print(msg1)
    print(msg2)
    rep_char('-', nstr * 2)

name = str(input('Input his/her name: '))
welcome_message(name)
