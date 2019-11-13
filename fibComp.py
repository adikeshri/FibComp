import numpy
import time
import matplotlib.pyplot as plt
X=[]
yFib=[]
yFibMemo=[]
def fib(n):
	if n==0 or n==1:
		return n
	return fib(n-1)+fib(n-2)
def fibMemo(n):
	if n==0 or n==1:
		return n
	if memo[n]!=-1:
		return memo[n]
	memo[n]=fibMemo(n-1)+fibMemo(n-2)
	return memo[n]

for i in range(1,30):
	print('Calculating for: ' + str(i))
	memo=[-1]*50
	start=time.time()
	x=fib(i)
	end=time.time()
	yFib.append(end-start)
	start=time.time()
	x=fibMemo(i)
	end=time.time()
	yFibMemo.append(end-start)
	X.append(i)
plt.plot(X,yFib,label='Without memoization')
plt.plot(X,yFibMemo,label='With memoization')
plt.ylabel('Execution time')
plt.xlabel('Value of n')
plt.title('Value of n vs Execution time')
plt.legend(loc='best')
plt.savefig('/home/adi/Downloads/www.adityakeshri.ml/beckham/images/comp1.png')
plt.show()