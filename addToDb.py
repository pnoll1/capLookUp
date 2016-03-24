# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 13:55:32 2016

@author: pnoll
"""

import sqlite3
crane = 'DemagAc615'
BoomType = 'SA'
Counterweight = 88000
Outrigger = 'Full'
BoomLen = 164
BoomAngle = None
JibLen = 39
JibAngle = 0
Radius = [33,39,46,52,59,65,72,79,85,92,98,105,111,118,124,131,138,144,151,157,164,170,177]
Capacity = [37500,37500,36600,3500,33200,31700,30200,28400,26900,25100,23500,22000,19100,16700,14300,12100,10300,8600,7500,5900,4600,3700,2600]
def addToDb(crane,BoomType, Counterweight,Outrigger,BoomLen,BoomAngle,JibLen,JibAngle,Radius,Capacity):
    conn = sqlite3.connect('crane.db')
    n = 0
    for x in Radius:
        conn.execute('INSERT INTO {0} VALUES (?,?,?,?,?,?,?,?,?)'.format(crane),(BoomType,Counterweight,Outrigger,BoomLen,BoomAngle,JibLen,JibAngle,Radius[n],Capacity[n]))        
        conn.commit()
        n = n+1
    conn.close()
addToDb(crane, BoomType, Counterweight, Outrigger, BoomLen, BoomAngle, JibLen, JibAngle, Radius, Capacity)
