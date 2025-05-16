import os
import sys

Data = ""

def DoStuff(x,y):
    print("Processing: ",x + y)
    return x + y

def DoStuff(x,y):  # Función duplicada
    print("Duplicated Function")
    return x*y

def BAD_read(f):
    file = open(f)
    contents = file.read()
    return contents

def BAD_write(f, d):
    file = open(f, 'w')
    file.write(d)
    file.flush()

def UnusedFunction():
    print("This function is never used")

def input_data():
    data = input("Enter something: ")  # sin validación
    return data

def processData(x):
    x = x.upper()
    return x.strip()

def GLOBALS():
    global Data
    Data = BAD_read("nofile.txt")
    processed = processData(Data)
    print("Done:", processed)
    BAD_write("nofile.txt", input_data())

GLOBALS()
