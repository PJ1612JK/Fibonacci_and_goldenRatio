# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 19:17:35 2020

@author: @pj1612jk
"""
import numpy as np
import matplotlib.pyplot as plt
def fib_plot(n):
    for i in range(len(n)):
        plt.errorbar(i, n[i], fmt='o')
    plt.xlabel('number of terms')
    plt.ylabel('$n^{th}$ term of Fibonacci Sequence')
    plt.title('First 30 terms of Fibonacci Sequence')
def gr_plot(gr):
    mean_gr=np.mean(gr)
    plt.axhline(mean_gr, color='red')
    plt.axhline(1.61803399, color='k', linestyle='dashed')
    for i in range(len(gr)):
        plt.errorbar(i,gr[i], fmt='s', mec='k', mfc='blue')
        plt.ylim(1,1.7)
    plt.title('Golden ratio calculated using 30 terms')
    plt.xlabel('number of iterations')
    plt.ylabel('golden ratio for n iterations')

def gr_evolve_plot(m,s,l):
    plt.errorbar(l, m, yerr=s, fmt='s', mec='k')
    plt.axhline(1.61803399, color='k', linestyle='dashed')
    plt.ylim(1.38,1.86)
    plt.xticks([1,2,3,4,5],['$10^1$','$10^2$','$10^3$','$10^4$','$10^5$'])
    plt.ylabel('Golden ratio calculated by taking the last 2 terms of sequence')
    plt.xlabel('Number of terms in the Fibonacci sequence')
    plt.title('Accuracy of golden ratio-plot 2')

def fib_generator(seed_1, seed_2):
    n_fib_no=seed_1+seed_2
    return n_fib_no
def golden_ratio_calculator(t_1,t_2):
    gr=(t_2/t_1)
    return gr
def main():
    l=len(fib_seq)
    t1=l-2
    t2=l-1
    nextnum=fib_generator(fib_seq[t1],fib_seq[t2])
    fib_seq.append(nextnum)
    gr=golden_ratio_calculator(fib_seq[t1],fib_seq[t2])
    gr_seq.append(gr)
fib_seq=[1,1]
gr_seq=[]
for i in range(30):
    main()
fib_plot(fib_seq)
gr_plot(gr_seq)

def gr_heavy(fs,gs):
    l=len(fs)
    t1=l-2
    t2=l-1
    nextnum=fib_generator(fs[t1],fs[t2])
    fs.append(nextnum)
    gr=golden_ratio_calculator(fs[t1],fs[t2])
    gs.append(gr)
for i in range(1,6):
    fs=[1,1]
    gs=[]
    limit=pow(10,i)
    for j in range(limit):
        gr_heavy(fs,gs)
    mean_gr=np.mean(gs)
    std_dev_gr=np.std(gs)
    L=len(gs)-1
    gr_evolve_plot(gs[L],std_dev_gr,i)

#plt.savefig('./fibonacci_series_30_terms.jpg')