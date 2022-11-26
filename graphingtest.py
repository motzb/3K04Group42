# importing the modules
import numpy as np 
import matplotlib.pyplot as plt 
#function takes in the time array and signal array
def graphdata(time, signal):
    #creates axis titles and graph title
    plt.title("Heart Signal") 
    plt.xlabel("time") 
    plt.ylabel("bpm") 
    #plots and shows the graph
    plt.plot(time, signal, color ="red") 
    plt.show()


#test case
x=[1,2,3,4,5,6]
y=[60,62,57,88,69,90]
graphdata(x,y)