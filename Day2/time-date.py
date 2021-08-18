import time
#miliseconds
t=time.time()
print(t)
#complete date/time info
d=time.localtime(t)
print(d)
#format date/time
r=time.asctime(d)
print(r)