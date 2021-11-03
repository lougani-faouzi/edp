#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import statistics as stat
import numpy as np
import matplotlib.pyplot as plt

y = []
X = [1,2,4,6,8]
for k in X:
    bw = []
    for i in range(1,6):
        with open(str(k)+"."+str(i)+".json", "r") as read_file:
            data = json.load(read_file)
            bw.append((data['jobs'][0]['read']['bw'] + data['jobs'][0]['write']['bw'])/2)
    y.append(stat.mean(bw))
print(y)

   
plt.plot(X, y, color='black', label='donnees aleatoires')
plt.xlabel("nombre de processus")
plt.ylabel("bande passante")
plt.show()


