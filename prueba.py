
import pandas as pd
from lectura import leer_csv, validar_calidad

libros_t = leer_csv('Archivos/ANALISIS DE COLECCIÓN - PRUEBA -reportresults.csv')

validar_calidad(libros_t)


libros_t2 = libros_t[['title','author','isbn']]
validar_calidad(libros_t2)

libros_t2 = libros_t2.drop_duplicates()
print(libros_t2.head(50))
print(libros_t2.info())

autor = libros_t2[libros_t2['author'] == 'Rabuffetti, Hebe T.']

print(autor)