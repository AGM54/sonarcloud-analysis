import os
import sys

Data = ""

def DoStuff(x, y):
    print("Processing: ", x + y)
    return x + y

def DoStuff(x, y):  # 🔁 Función duplicada
    print("Duplicated Function")
    return x * y

def BAD_read(f):
    file = open(f)
    contents = file.read()
    return contents  # ⚠ No se cierra el archivo

def BAD_write(f, d):
    file = open(f, 'w')
    file.write(d)
    file.flush()  # ⚠ No se cierra el archivo correctamente

def UnusedFunction():
    print("This function is never used")  # ⚠ Código muerto

def input_data():
    data = input("Enter something: ")  # ⚠ Input sin validación
    return data

def processData(x):
    x = x.upper()
    return x.strip()

def insecure_system_call():
    user_input = input("Enter a command: ")
    os.system(user_input)  # 🔥 Security Hotspot: comando arbitrario

def dangerous_eval():
    user_code = input("Enter Python code to run: ")
    eval(user_code)  # 🔥 Security Hotspot crítico

def read_sensitive_file():
    with open("/etc/passwd", "r") as file:
        data = file.read()
    print("System users:", data)  # ⚠ Información sensible

def GLOBALS():
    global Data
    Data = BAD_read("nofile.txt")
    processed = processData(Data)
    print("Done:", processed)
    BAD_write("nofile.txt", input_data())
    insecure_system_call()
    dangerous_eval()
    read_sensitive_file()

GLOBALS()
