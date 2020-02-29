import numpy as np 
import matplotlib.pyplot as plt 
from numpy import random 


def picture_result(f,a,b,maximum,args):
    xs=np.arange(a,b,0.1)
    plt.figure(figsize=(15,3))
    plt.plot(xs,list(map(f,xs)))
    plt.plot(xs, np.zeros(xs.shape),color='black',linewidth=1)
    plt.plot(maximum,0,'.',marker="*",color='red')
    plt.savefig(args.path + "/maximum.eps")