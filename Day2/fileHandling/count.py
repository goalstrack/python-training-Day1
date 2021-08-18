
fn=input('Enter File Name. ')

f=open(fn,'r')

st=f.read(2000)
words,digits,loc,upc=0,0,0,0
for i in st:
    if i.isdigit():
        digits=digits+1
    if i.islower():
        loc=loc+1
    if i.isupper():
        upc=upc+1
    if i.isspace():
        words=words+1
print("No of digits: ",digits,"\n No of Lower case character ",loc,"\n No of upper case character ",upc,"\n No of spaces ",words)



f.close()