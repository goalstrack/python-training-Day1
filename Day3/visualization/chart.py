
import matplotlib.pyplot as plt
import numpy as np

ct=['india','USA','UK']
pop=[1.35,1.80,1]
y=np.arange(len(ct))
plt.barh(y,pop)#horizontal bar
plt.xticks(y,ct)
plt.title('pop chart')
plt.show()
