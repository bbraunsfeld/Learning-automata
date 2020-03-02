import numpy as np 
import matplotlib.pyplot as plt 
from numpy import random 


def picture_result(optim,f,a,b,optimum,args):
    xs=np.arange(a,b,0.1)
    plt.figure(figsize=(15,3))
    plt.plot(xs,list(map(f,xs)))
    plt.plot(xs, np.zeros(xs.shape),color='black',linewidth=1)
    plt.plot(optimum,0,'.',marker="*",color='red')
    plt.axvline(x=optimum,ls='--',color='red')
    if optim == 'max':
        plt.savefig(args.path + "/maximum.eps")
    elif optim == 'min':
        plt.savefig(args.path + "/minimum.eps")

def picture_results(f,a,b,minimum,maximum,args):
    xs=np.arange(a,b,0.1)
    plt.figure(figsize=(15,3))
    plt.plot(xs,list(map(f,xs)))
    plt.plot(xs, np.zeros(xs.shape),color='black',linewidth=1)
    plt.plot(minimum,0,'.',marker="*",color='red')
    plt.axvline(x=minimum,ls='--',color='red')
    plt.plot(maximum,0,'.',marker="*",color='blue')
    plt.axvline(x=maximum,ls='--',color='blue')
    plt.savefig(args.path + "/minmax.eps")
