import math
marks1=float(input("Enter ur marks"))
marks2=float(input("Enter ur marks"))
marks3=float(input("Enter ur marks"))
marks4=float(input("Enter ur marks"))
marks5=float(input("Enter ur marks"))
marks6=float(input("Enter ur marks"))


def calmean():
   
    mean=(marks1+marks2+marks3+marks4+marks5+marks6)/6
    
    return mean

def calvar():
    var=((mean-marks1)**2+(mean-marks2)**2+(mean-marks3)**2+(mean-marks4)**2+(mean-marks5)**2+(mean-marks6)**2)/5
    #we can use passing variable if we declare it in middle weuse variable passing and we should use same var inside the funation to that in "def functionname(variable)" 
    return var 

def calsd():
    sd=math.sqrt(((mean-marks1)**2+(mean-marks2)**2+(mean-marks3)**2+(mean-marks4)**2+(mean-marks5)**2+(mean-marks6)**2)/5)
#sd=math.sqrt(var) =>since we use global variabls here for input no need to pass variables
    return sd 


mean=calmean()
var=calvar()
sd=calsd()
print("Average marks is",mean)
print("Variance of marks is",var)
print("Standard deviation of marks is",sd)
