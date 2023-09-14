from hermite import hermiteEq as h
import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
import json
plt.style.use('seaborn-whitegrid')

class q_oscilator:
    """
    By: Juan Esteban Ospina Holguin - 2023


    This class make a solution to wave function for an quantun oscilator and make a plot from it
    parameters:
    a: float - lower limit of the integral
    b: float - upper limit of the integral
    n: int - order of the hermite polynomial
    k: float - spring constant
    m: float - mass of the particle

    return:
    plot: plot - plot of the wave function
    """
    def __init__(self):
        with open("config.json","r") as file:
            data = json.load(file)
        self.a = data["a"]
        self.b = data["b"]
        self.n = data["n"]
        self.k = data["k"]
        self.m = data["m"]
        self.i = data["i"]
        self.hbar = data["hbar"]

    def alpha(self):
        """This method calculate the alpha parameter"""
        return np.sqrt(np.sqrt(self.m*self.k)/self.hbar)

    def potential(self):
        """This method calculate the potential function"""
        V = lambda x: 0.5*self.k*x**2
        return V
    
    def N(self,n):
        """This method calculate the normalization constant"""
        return (2**n*np.math.factorial(n))**-0.5*np.pi**-0.25

    def oscilator_solution(self,i):
        """This method calculate the wave function"""
        psi = lambda x: self.N(i)*(h(i).solution_hermite())(self.alpha()*x)*np.exp(-self.alpha()*x**2/2)
        return psi
    
    def Energy(self,e):
        """This method calculate the energy of the particle"""
        return (e + 0.5)*self.hbar*np.sqrt(self.m/self.k)
    
    def plot(self):
        """This method make a plot of the wave function"""
        try:
            x = np.linspace(self.a,self.b,self.i)
            pot = self.potential()
            plt.figure(figsize=(10, 6))
            plt.plot(x,pot(x),label = "Potencial")
            for i in self.n:
                func = self.oscilator_solution(i)
                plt.plot([self.a,self.b],[self.Energy(i),self.Energy(i)],label = "$E_{} = {} h \omega$".format(i,self.Energy(i)),linestyle = "--")
                plt.plot(x,func(x)**2+self.Energy(i))
            plt.xlabel("x")
            plt.ylabel("$|\Psi(x)|^2$")
            plt.title("Quantum oscilator")
            plt.legend(loc='center left', bbox_to_anchor=(0.945, 0.5))
            plt.savefig("QO.png")
            return True
        except:
            print("Error in the plot")
    
    def run(self):
        """This method run the program"""
        print("welcome to the quantum oscilator")
        print("running...")

        self.plot()

        print("The file has been saved as QO.png")
        return True
