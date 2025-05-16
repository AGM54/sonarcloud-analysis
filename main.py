import os

def rf(fp):
    f = open(fp)
    d = f.read()
    f.close()
    return d

def wf(fp, d):
    f = open(fp, 'w')
    f.write(d)

def gui():
    return input()

def pd(d):
    return d.lower()

def Main():
    # uso de variable global innecesaria
    global FilePath
    FilePath = "example.txt"

    # lectura insegura de archivo sin manejo de errores
    d = rf(FilePath)

    # procesamiento sin validación de datos
    pd(d)

    # escribir archivo sin cerrar ni validar entrada
    ui = gui()
    wf(FilePath, ui)

Main()
