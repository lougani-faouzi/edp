#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import statistics as stat
import numpy as np
import matplotlib.pyplot as plt


X = [1,2,3,4,5]
bw = []
for i in range(1,6):
   with open(str(i)+".json", "r") as read_file:
        data = json.load(read_file)
        bw.append((data['jobs'][0]['read']['bw'] + data['jobs'][0]['write']['bw'])/2)

   
plt.plot(X, bw, color='black', label='donnees aleatoires')
plt.xlabel("nombre de repetitions")
plt.ylabel("bande passante")
plt.show()


