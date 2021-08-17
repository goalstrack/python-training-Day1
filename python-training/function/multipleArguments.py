def showdata(*x):
    print('show data')
    for m in x:
        print('value.. ',m)
    print(type(x))

showdata(10)
showdata(32,43)
showdata(32,43,43)
showdata(12,43,43,54)
showdata('ay',43,'xyx',80)