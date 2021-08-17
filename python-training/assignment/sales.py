sale=float(input('Enter the sale '))
if sale>10000:
    newsale=sale-(0.15*sale)
else:
    newsale=sale-(0.10*sale)
print(newsale)