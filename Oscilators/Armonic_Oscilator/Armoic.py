#Armonic Motion
#Author: Juan Ospina H <juan.ospina25@udea.edu.co>


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class particle:
    """Class that defines a particle
    
    Attributes:
        mass (float): mass of the particle
        l (float): lenght of the spring
        time (float): time of the simulation
    """

    def __init__(self,mass,lenght,time):
        self.mass = mass
        self.l = lenght
        self.time = time
        self.theta = lambda A,t: A*np.cos(t) #Function that defines the armonic motion
    
    def armonic(self):
        """Function that calculates the armonic motion of the particle"""
        A = np.sqrt(2*self.mass*self.l)
        t = np.linspace(0,self.time,100)
        angle = np.array([self.theta(A,i) for i in t])
        return angle