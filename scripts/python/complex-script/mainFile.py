import os
import script1
import script2

def main():
    print("Ejecutando el archivo principal 'mainFile.py'")
    
    # Llamada a script1.py
    result1 = script1.function_script1("argument-1")
    print(f"Resultado de script1: {result1}")
    
    # Llamada a script2.py
    result2 = script2.function_script2("argument-2")
    print(f"Resultado de script2: {result2}")

if __name__ == "__main__":
    main()