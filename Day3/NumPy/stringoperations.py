import numpy as np

x='this is PYTHON'

print(np.char.lower(x))

print(np.char.upper(x))

print(np.char.title(x))
print(np.char.capitalize(x))
print(np.char.multiply('Hello',5))

print(np.char.add('Hello','Python'))

r=np.char.replace(x,'this','that')
print(r)