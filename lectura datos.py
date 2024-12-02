import pandas as pd

def lectura(ruta_archivo):
    # Leer el archivo directamente en un DataFrame de pandas
    data = pd.read_csv(ruta_archivo, encoding='utf-8', header=0)
    
    nombre_archivo= input("Ingrese el nombre del archivo a guardar: ")
    # Guardar el DataFrame en un archivo Excel
    data.to_excel(nombre_archivo + ".xlsx", index=False)

ruta_acceso= input("Ingrese ruta de acceso: ")
# Llamar a la función usando la ruta al archivo
lectura(ruta_acceso + ".csv")
