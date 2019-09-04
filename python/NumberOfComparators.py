import matplotlib.pyplot as plt
import numpy as np

N = 352
xafter2 = 32
xstep = 32

input = np.arange(2,N+1)
comparators = [i*(i-1)/2 for i in input]
plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.plot(input,comparators)
plt.xlabel(r"Number of inputs ($I$)")
plt.ylabel(r"Number of comparators ${I\choose 2}$")
plt.xlim((2,N))
xticks = np.concatenate(([2],np.arange(xafter2,N+1,xstep)))
plt.xticks(xticks,xticks)
plt.title(r"Number of comparators ${I\choose 2}$ vs number of inputs ($I$)")
plt.show()
#plt.savefig('NumberOfComparators.pdf',bbox_inches='tight')
plt.close()