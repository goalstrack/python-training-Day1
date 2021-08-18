try:
    a=int(input('Enter a number'))
    if a<10:
        raise Exception()
    else:
        print('ok')
except:
    print('any issue')
finally:
    print('end')