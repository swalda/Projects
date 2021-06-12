import math
import numpy as np
import matplotlib.pyplot as plt

def fac(n):
    return math.factorial(n)

def func(x, coef):
    res = 0
    for i in range(0, coef.size):
        res += x**i * coef[i]
    return res

def itteration(x,n): # x - point, n - diviadtion
    res = x**2
    i = 1
    b = x**2 * math.cos(x)
    while (abs(b-res)) > n:
        i += 1
        if i%2 == 1:    
            res += ((x**2)**i)/(fac(2*(i-1)))
        else:
            res -= ((x**2)**i)/(fac(2*(i-1)))
    return i*2 + 1

def coef(n):
    res = np.zeros(n)
    res[0] = 0
    for i in range(1, n):
        if i%2 == 0:
            if (i/2)%2 != 0:
                res[i] = 1/fac(i-2)
            else:
                res[i] = -1/fac(i-2)
        else:
            res[i] = 0
    return res
        


print("Необходимо задать точность - степень десяти(без минуса)")
b = int(input())
c = int(itteration(1, 10**(-b)))

print("Для заданной точности необходимо членов разложения:", c)
a = np.zeros(100)
for i in range(0,100):
    a[i] = (10**(-b))
    

coef1 = coef(itteration(1, 10**(-b)))
coef2 = coef(itteration(1, 10**(-b)) - 2)

x = np.linspace(-1, 1, 100, endpoint=True)
plt.plot(x,a)

print("Коеф-ты разложения:")
print(coef1)
print(coef2)


err = np.zeros(100)
for i in range(0, 100):
    err[i] = abs((x[i]**2)*math.cos(x[i]) - func(x[i], coef1))

#plt.plot(x, err, ls="--", label=str(c))

err1 = np.zeros(100)
for i in range(0, 100):
    err1[i] = abs((x[i]**2)*math.cos(x[i]) - func(x[i], coef2))
    
#plt.plot(x, err1,ls="--", label=str(c-1))

plt.legend()
plt.show

print("производим экономизацию")
coef1[9] += 2816/(1024*fac(11))
coef1[7] += -2816/(1024*fac(11))
coef1[5] += 1232/(1024*fac(11))
coef1[3] += -220/(1024*fac(11))
coef1[1] += 11/(1024*fac(11))
coefeco10 = np.zeros(10)
for i in range(0, 10):
    coefeco10[i] = coef1[i]
    
plt.plot(x, a)
for i in range(0, 100):
    err[i] = abs((x[i]**2)*math.cos(x[i]) - func(x[i], coefeco10))

plt.plot(x, err, ls="-.", label=str(c))

plt.show
    

