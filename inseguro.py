import os

def insecure_system_call():
    user_input = input("Enter a filename to delete: ")
    os.system(f"rm -rf {user_input}")  # 🔥 Vulnerabilidad: comando del sistema basado en input

def dangerous_eval():
    code = input("Enter Python code to evaluate: ")
    eval(code)  # 🔥 Vulnerabilidad crítica: ejecución arbitraria

def read_sensitive_file():
    with open("/etc/passwd", "r") as file:
        content = file.read()
    print("User data:", content)  # 🔥 Riesgo: exposición de información sensible

def write_file_from_input():
    data = input("What do you want to write to the file?: ")
    with open("output.txt", "w") as f:
        f.write(data)  # ⚠️ Si el input es controlado, puede causar persistencia insegura

insecure_system_call()
dangerous_eval()
read_sensitive_file()
write_file_from_input()
