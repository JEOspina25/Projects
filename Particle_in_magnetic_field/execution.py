from particle import particle 
if __name__ == "__main__":

    #Parameters
    E = 18.6 #ev. Energy
    angle = 30 # ° . Angle between tajectory and direction of magnetic field
    m = 9.109e-31 # kg. electron mass 
    B = 600e-6 #T. Magnetig field intensity
    time = 0.000002 #s . Time 
    n = 10000 #steeps
    particle_type = "Electron"
    q = 1.6022e-19 #C. charge

    #Assignament
    electron = particle(E,angle,m,B,time,n,q, particle_type)


    #Run
    electron.figPlot()

    #Feedback
    print("\033[1;32m"+"Welcome! \nRunning..."+'\033[0;m')
    print("cilotron frequency: {} Hz".format(electron.wc()))
    print("speed at t=0 V = {} m/s".format(electron.V()[3]))
    print("Radius of the spiral = {} m".format(electron.radious()))
    

    
