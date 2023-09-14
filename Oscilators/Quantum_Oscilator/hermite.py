import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

class hermiteEq:
    """
    By: Juan Esteban Ospina Holguin - 2023
    This class make a solution to wave function for an quantun oscilator and make a plot from it
    parameters:
    n: int - order of the hermite polynomial

    return:
    hermite: function - function that return the hermite polynomial
    """
    
    def __init__(self,n):
        """This method initialize the parameters of the class"""
        self.n = n

    def solution_hermite(self):
        """This method make a solution to the hermite equation"""
        z = sym.Symbol('z')        
        derivada = sym.diff(sym.exp(-z**2),z,self.n)
        H = (-1)**self.n * sym.exp(z**2)* derivada
        H = sym.lambdify(z,H,"numpy")
        return H


    
