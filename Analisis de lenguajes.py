import re
print("Directorio donde se encuentra el archivo + [nombre del archivo y extencion] ejemplo: c:/carpeta/index.php")
dir = input("Buscar: ")
patron1 = r"(\w+\s\=)"
patron2 = r"([0-9]{1,3}$|[0-9]{1,3}\.[0-9]{1,3}$)"
patron3 = r"(\*\*)|[\*\/\%\+\-]"
patron4 = r"(\=\=)|(\!\=)|\<[\d|\w]|\<\s[\d|\w]|\>[\d|\w]|\>\s[\d|\w]|(\<\=)|(\>\=)"
patron5 = r"(class)|(def)|(end)|(puts)|(if)|(else)|(new)"

contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0
contador5 = 0

f = open(dir, "r")
print("")
print("Variables validas")
while(True):
    linea = f.readline()
    contador1 = contador1 + 1
    coincidencias1 = re.findall(patron1, linea)
    for coincidencia1 in coincidencias1:
        print(f"Linea {contador1} se encontro {coincidencia1}")

    if not linea:
        break
f.close()

f = open(dir, "r")
print("")
print("Numeros decimales y enteros")
while(True):
    linea = f.readline()
    coincidencias2 = re.findall(patron2, linea)
    contador2 = contador2 + 1
    for coincidencia2 in coincidencias2:
        print(f"Linea {contador2} se encontro {coincidencia2}")

    if not linea:
        break
f.close()

f = open(dir, "r")
print("")
print("Operaciones aritmeticas")
while(True):
    linea = f.readline()
    contador3 = contador3 + 1
    coincidencias3 = re.findall(patron3, linea)
    for coincidencia3 in coincidencias3:
        print(f"Linea {contador3} se encontro {coincidencia3}")

    if not linea:
        break
f.close()

f = open(dir, "r")
print("")
print("Operaciones condicionales")
while(True):
    linea = f.readline()
    contador4 = contador4 + 1
    coincidencias4 = re.findall(patron4, linea)
    for coincidencia4 in coincidencias4:
        print(f"Linea {contador4} se encontro {coincidencia4}")

    if not linea:
        break
f.close()

f = open(dir, "r")
print("")
print("Palabras reservadas")
while(True):
    linea = f.readline()
    contador5 = contador5 + 1
    coincidencias5 = re.findall(patron5, linea)
    for coincidencia5 in coincidencias5:
        print(f"Linea {contador5} se encontro {coincidencia5}")

    if not linea:
        break
f.close()
print("")
print("----------Luis Miguel Chan----------")
print("")