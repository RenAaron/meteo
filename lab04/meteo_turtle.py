import meteo
from turtle import *

def init():
    meteo.background()
    penup()
    speed(0)

def process_S():
    """
     processes an S command (sun) command in meteo turtle
    """
    meteo.draw_sun()

def process_C():
    """
    processes a C command (cloud) command in meteo turtle
    """
    meteo.draw_cloud()

def process_P():
    """
    processes a P command (cloudy sun) command in meteo turtle
    """
    meteo.draw_sun()
    meteo.draw_cloud()

def process_R():
    """
    processes an R command (rainy cloud) command in meteo turtle
    """
    meteo.draw_cloud()
    meteo.draw_rain()

def process_A(stri):
    """
    processes an A (circle) command in meteo turtle
    returns the amount of steps taken
    """
    n = 0
    n += 1
    r = getNumber(stri[n:])
    n += len(r) - 1
    color("red")
    pendown()
    width(2)
    circle(int(r))
    width(1)
    penup()
    return n

def process_T(stri):
    """
    processes a T (temperature) command in meteo turtle
    returns the amount of steps taken
    """
    n = 0
    n += 1
    t1 = getNumber(stri[n:])
    n += len(t1) - 1
    color("white")
    begin_fill()
    meteo.draw_rectangle(36, 16)
    end_fill()
    color("black")
    write(t1 + "F")
    return n

def process_G(stri):
    """
    processes a G (go to) command in meteo turtle
    returns the amount of steps taken
    """
    n = 0
    n += 1
    x1 = getNumber(stri[n:])
    n += len(x1) + 1
    y1 = getNumber(stri[n:])
    n += len(y1) - 1
    goto(int(x1), int(y1))  # RG100,100
    return n

def getNumber(stri):
    """
    returns number of the first characters input as a string as a string
    """
    rv = ""
    for x in stri:
        if(x.isdigit() or x == "-"):
            rv += x
        else:
            return rv



def interpret(stri):
    """
    scans through each character of the string input and interprets them as meteo turtle commands and actions
    S - Draws sun
    C - Draws cloud
    P - Draws cloudy sun
    R - Draws rainy cloud
    W - Draws snowy cloud
    A - Draws circle of specified radius
    T - Draws temperature
    G - Goes to certain location on map
    """
    n = 0
    while(n<=len(stri)-2):
        if(stri[n] == "S"):
            try:
                process_S()
            except:
                print("There was an error with S")
        elif (stri[n] == "C"):
            try:
                process_C()
            except:
                print("There was an error with C")
        elif (stri[n] == "P"):
            try:
                process_P()
            except:
                print("There was an error with P")
        elif (stri[n] == "R"):
            try:
                process_R()
            except:
                print("There was an error with R")
        elif (stri[n] == "W"):
            try:
                meteo.draw_snow()
            except:
                print("There was an error with W")
        elif (stri[n] == "A"):
            try:
                n += process_A(stri[n:])
            except:
                print("There was an error with A")
        elif (stri[n] == "T"):
            try:
                n += process_T(stri[n:])
            except:
                print("There was an error with T")
        elif(stri[n] == "G"):
            try:
                n += process_G(stri[n:])
            except:
                print("There was an error with G")

        else:
            print("Invalid command character")
            break
        n += 1


def main():
    init()
    interpret(input("Give meteo command: ")+"*")
    done()

if(__name__ == "__main__"):
    main()
