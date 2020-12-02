print("Directorio donde se encuentra el archivo + [nombre del archivo y extencion] ejemplo: c:/carpeta/index.php")
dir = input("Buscar")
f = open(dir, "r")
while(True):
    linea = f.readline()
    print(linea)
    if not linea:
        break
f.close()