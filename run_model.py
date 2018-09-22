import matplotlib.pyplot as plt
import numpy
import math
import random



people = [1000 for i in range(500)]
total = []
for i in range(1500):
    n = random.randint(0,499)
    m = random.randint(0,499)
    x = people[n] #Whether x or y is gaining money depends on the random fraction generated
    y = people[m]  
    if x > 0 and y > 0 and n != m:
        pool = x + y
        exchange = random.random()*pool
        
        
        people[n] = exchange
        people[m] = pool-exchange  
    wealth = sum(people)
    total.append(wealth)
plt.figure(0)
    
plt.hist(people)
plt.xlabel("Wealth")
plt.ylabel("Number of People")
plt.title("1500 trials")

plt.legend()
plt.savefig("Histogram.png")
plt.figure(1)
plt.hist(people)
plt.xlabel("Wealth")
plt.ylabel("Number of People")
plt.title("1500 trials")
e = math.e
a = numpy.linspace(0,10000,1000)
b = 230*e**((-1/1000)*a) #scaling factor near value of most wealthy persons and 1/m_initial is 1/1000


plt.plot(a,b,label = "Gibbs Distribution")
plt.legend()
plt.savefig("Histogram_and_curve.png")


plt.figure(2)
l = len(total)
plt.plot(numpy.linspace(0,l-1,l),total)
plt.ylim(0,1000000)
plt.xlabel("time")
plt.ylabel("Wealth Total")
plt.title("Total Check")
plt.savefig("Total_Check.png")
plt.tight_layout()
plt.show()
