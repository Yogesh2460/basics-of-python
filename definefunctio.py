def myprint():
    print("hello")
    print("hajime mashite")
myprint()


"""def printage(inval):
    print(inval)


var=raw_input("enter ur age")
printage(var)   #here value is passing from calling fun


def printage(inval):
    inval="my age is 50" #this value will be going to print
    print(inval)
var=raw_input("enter ur age")
printage(var)   #here value is not passing from calling fun



def printage(inval):
    print(inval)
var=int(raw_input("enter ur age")) #var is declared as int unlike above where it is int
printage(var)   #here value is passing from calling fun



def printage(inval):
    print("my age is" inval)
def addsub(a,b)
    return a+b,a-b#return 2 results at once

var=int(raw_input("enter ur age"))
printage(var)   #here value is passing from calling fun
"""
"""
def muldiv(a,b):
    mul=a*b
    div=a/b
    return mul,div


a=int(raw_input("enter ur no"))
b=int(raw_input("enter ur no"))
muldiv(a,b)
print("multiplication is",mul)

print("quotient is",div)
"""


def muldiv():
     a=int(input("enter 1st no:"))
     b=int(input("enter 1st no:"))
     mul=a*b
     div=a/b
     print(id(mul))#inside fun mul is not same as outside mul but they point to same location
     return mul,div

mul,div=muldiv()
print(id(mul))#heap helps in point same locan with help oftwo pointers
print("multiplication is",mul)

print("quotient is",div)
 
