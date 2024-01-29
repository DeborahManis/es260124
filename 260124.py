def my_fun():
    x = do_it()
    print(x)
    
def do_it():
    return "temporary fake value"
my_fun()

def input_number(message: str):
    try: 
         x = input(message)
         if x:
             return float(x)
         return None
    except: 
        print("non hai digitato un numero, quindi termino l inserime")



def populate_list(l: []):
    x = 0
    while x !=None:
        x= input_number("Nuovo numero:  ")
        if x !=None:
            l.append(x)
            

list = []
populate_list(list)
print(list)
    
                 
from matplotlib import pyplot as ptl
from numpy import random as rnd
import humanize as h

data =  rnd.randint(0, 100, 10)
x = [h.ordinal(i) for i in range(1, 16)]
ptl.plot(  x )


from matplotlib.lines import lineStyles
import numpy as np
import humanize as h
import pandas as pd
import matplotlib.pyplot as plt
stockdata = pd.read_csv (r'C:\Users\Debor\Downloads\stockdata.csv ')
#print(stockdata)
msft = stockdata ['MSFT']
date = pd.to_datetime(stockdata['Date'])          
#print(msft, date)

plt.figure(figsize=(6, 4))
plt.plot(date, msft, label='Andamento azioni MSFT', color='m',)
plt.title('Andamento azioni Microsoft nel tempo', color='blue')
plt.xlabel('data')
plt.ylabel('Valore')
plt.legend()
plt.show()

prime5 = msft.head(5)
primeDate = date.head(5)
#print(prime5, primeDate)

ultime5 = msft.tail(5)
ultimeDate= date.tail(5)
#print(ultime5, ultimeDate)

#uniamo i dati e facciamo il grafico

msft5 = pd.concat([prime5 , ultime5])
date5= pd.concat([primeDate , ultimeDate])
print(msft5, date5)

plt.figure(figsize=(6, 4))
plt.plot(date5, msft5, label='Andamento azioni MSFT', color='m',)
plt.title('Andamento azioni Microsoft nel tempo', color='blue')
plt.xlabel('data')
plt.ylabel('Valore')
plt.legend()
plt.show()

Estraiamo le prime 20 istanze della colonna AAPL delle azioni di Apple

apple= stockdata['AAPL']
apple20 = apple.head(20)
date20= date.head(20)

print(apple20,date20)
plt.figure(figsize=(6,4))
plt.plot(date20, apple20, marker='o', linestyle = '--', color = 'r',markersize=8, markerfacecolor='black',linewidth='2',label= 'azioni Apple')
plt.title('Azioni Apple')
plt.xlabel('Data')
plt.ylabel('Valore')
plt.legend()
plt.show()
azioni = stockdata[['MSFT','IBM', 'SBUX', 'AAPL', 'GSPC']]
azioni20 = azioni.head(20)
plt.figure(figsize=(6,4))
plt.plot(date20, azioni20['MSFT'], label='MSFT')
plt.plot(date20, azioni20['IBM'], label='IBM')
plt.plot(date20, azioni20['SBUX'], label='SBUX')
plt.plot(date20, azioni20['AAPL'], label='AAPL')
plt.plot(date20, azioni20['GSPC'], label='GSPC')
plt.title('Azioni')
plt.xlabel('Data')
plt.ylabel('Valore')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.show()
