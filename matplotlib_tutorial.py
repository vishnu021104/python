import sys
import matplotlib
matplotlib.use("agg")

import matplotlib.pyplot as plt
import numpy as np

xpoints=np.array([1,7])
ypoints=np.array([1,10])

plt.plot(xpoints,ypoints)
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()