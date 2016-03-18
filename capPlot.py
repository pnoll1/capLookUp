import sqlite3
import matplotlib
import numpy as np
from matplotlib import pyplot as plt
def queryDb(column, crane, cwt):
    conn = sqlite3.connect('crane.db')        
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT {} FROM {} WHERE counterweight = {}".format(column, crane, cwt))
    x=[]
    for row in c:
        x.append(row[0])
    return x
crane = 'DemagAc435'
x = queryDb('Radius', crane, 59500)
y = queryDb('Capacity', crane, 59500)
plt.plot(x,y)
plt.show()