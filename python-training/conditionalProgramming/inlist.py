list=['pune','mumbai','kolkata','latur']

a=input('city.. ')

if a in list:
    print('Error')
else:
    list.append(a)
    print(list)