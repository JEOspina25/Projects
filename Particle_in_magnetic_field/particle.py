import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn")


class particle:
    """
    This code makes a plot of a particle on a magnetic field
    
    Parameters:
    * E : Energy of the particle (float) [ev]
    * ang : angle between field direction and particle direction (float) [°]
    * m : particle mass (float) [kg]
    * B : magnetic field intensity (float) [T]
    * time : evolution time of the process. This need to be very small ~e-6s (float) [s]
    * n : number of steeps to run the code (int) 
    * paticle_type : type of the particle (str)
    * q : charge of the particle (float) [C]

    Note: Make sure the units are consistent.
    """
    def __init__(self,E,ang,m,B,time,n, q, particle_type ):
        try:
            self.E=E/6.242e18
            self.ang=np.deg2rad(ang)
            self.m=m*2
            self.B = B
            self.n=n
            self.q = q #Carga del electron
            self.c =299792458
            self.time = time #seg
            self.particle_type = particle_type
        except:
            print("ERROR: check the type of variables")

    def wc(self):
        """
        ciclotronic frecuence
        """
        try:
            a = 1/self.B
            w = self.q*self.B/self.m
            return w
        except:
            print("ERROR: invalit parameter q, B, m")
    
    def V(self):
        try:
            v = np.sqrt(2 * self.E / self.m) #Velocidad neta
            v0x,v0y,v0z = v*np.sin(self.ang), 0, v*np.cos(self.ang)
            if v > 0.5*self.c:
                print("v = ",round(v/self.c,3),"c")
                print("WARNING: very high speed, it could leave the non-relativistic limit.")
        except:
            print("ERROR: the speed could not be calculated. Check the parameters E, m, ang")
        return v0x,v0y,v0z,v
    
    def r(self):
        try:
            t = np.linspace(0,self.time,self.n) #time 0 to t with n partitions
            x = (self.V()[0]/self.wc()) * np.sin(self.wc()*t)
            y = (self.V()[0]/self.wc()) * (np.cos(self.wc()*t) - 1)
            z = self.V()[2]*t
            return x,y,z

        except:
            print("ERROR: the position vector could not be calculated. Check the parameters")

    def radious(self):
        try: 
            rad = self.V()[0]/self.wc()
            return rad
        except:
            print("ERROR: invalit parameter q, B, m")

    
    def figPlot(self):
        fig = plt.figure(figsize = (10,5))
        ax = plt.axes(projection='3d')
        title = r'{}. $B = {} T$. $E$ = ${} ev$. $\theta = {}°$'.format(self.particle_type, round(self.B,6),round(self.E*6.242e18,3),round(np.rad2deg(self.ang),2))



        try: 
            x,y,z = self.r() #Se llama la funcion Runge Kutta
        
        except:
            print("ERROR: trajectory function fail()")
        try:    
            ax.plot(x,y,z,label = "Trajectory",color = "darkviolet")
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_zlabel('z')
            ax.quiver(0, -self.V()[0]/self.wc(), 0, 0, 0 , 
                    self.r()[2][-1], color='blue', label='$B$', pivot='tail',arrow_length_ratio=0.005)
            ax.view_init(30, 35)
            ax.set_title(title)
            ax.legend()
            plt.savefig("Trajectory.png")
        except:
            print("ERROR: Plotting is not possible. Check the parameters.")

    
