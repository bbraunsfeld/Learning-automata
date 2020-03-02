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
