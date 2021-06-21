# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 12:15:39 2021

@author: Kir
"""
import numpy as np
import random
import matplotlib.pyplot as plt

num_toss = 200 #number of coin tosses in one experiment
num_experiments = 1000 #number of experiments

def coin(toss_num):
    """This function returns a list of 'toss_num' coin tossing outcomes"""
    tosses = []
    for i in range(toss_num):
        tosses.append(random.randint(0, 1))
    return tosses

def max_run(toss_list):
    """This function returns a longest run of heads in a list of tossing outcomes"""
    max_seq = 0
    seq = 0
    for i in toss_list:
        if i == 1:
            seq += 1
            if seq > max_seq:
                max_seq = seq
        else:
            seq = 0
    return max_seq


longest_run = []
for j in range(num_experiments):
    toss_list = coin(num_toss)
    longest_run.append(max_run(toss_list))
print(longest_run)

bins = np.arange(2, max(longest_run) + 1, 1) - 0.5
plt.hist(longest_run, bins = bins, color='White', edgecolor='Black')
plt.xticks(np.arange(2, max(longest_run) + 1, 1))
plt.show()
