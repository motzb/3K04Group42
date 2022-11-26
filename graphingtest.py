# importing the modules
import numpy as np 
import matplotlib.pyplot as plt 
#function takes in the time array and signal array
def graphdata(time, signalatr,signalvent):
    #plots and shows the graph
    fig, axs = plt.subplots(2) 
    axs[0].plot(time,signalatr)
    axs[0].set_title("Atrial Signal")
    axs[0].set(xlabel="time")
    axs[0].set(ylabel="heart signal")
    axs[1].plot(time,signalvent)
    axs[1].set_title("Ventricle Signal")
    axs[1].set(xlabel="time")
    axs[1].set(ylabel="heart signal")
    plt.tight_layout()
    plt.show()

#test case
x=[1,2,3,4,5,6]
y=[0,62,57,88,69,90]
y2=[60,62,57,88,69,90]
graphdata(x,y,y2)