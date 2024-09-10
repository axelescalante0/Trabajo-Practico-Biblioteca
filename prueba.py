from lectura import leer_csv, validar_calidad
from conversor import convertir_isbn
import pandas as pd

libros_t = leer_csv('Archivos/ANALISIS DE COLECCIÓN - PRUEBA -reportresults.csv')

validar_calidad(libros_t)


libros_t2 = libros_t[['title','author','isbn']]
validar_calidad(libros_t2)

libros_t2 = libros_t2.drop_duplicates()
print(libros_t2.head(50))
print(libros_t2.info())



# Agrupar por título y autor, y contar cuántas veces aparece cada ISBN
libros_isbn = libros_t2.groupby(['title', 'author']).size().reset_index(name='count')


# Filtrar los que tienen un count mayor a 1
libros_repetidos = libros_isbn[libros_isbn['count'] > 1]

# Mostrar los libros que tienen más de un ISBN
print(libros_repetidos.info())

autor = libros_t2[libros_t2['title'] == 'Circuitos electrónicos :']

print(autor)

new_libros = convertir_isbn(libros_t2,'isbn')
a = new_libros[new_libros['title'] == 'Circuitos electrónicos :']


#Libros con los ISBN convertidos a 13 digitos
print(new_libros.info())

# Separar los ISBNs si están separados por espacio o "|", quedándonos con el primero
new_libros['isbn'] = new_libros['isbn'].str.split('|').str[0].str.strip()

# Verificar el resultado
#print(new_libros.head(50))


new_libros = convertir_isbn(new_libros,'isbn') #De nuevo convertimos los ISBN a 13 digitos luego de hacer el split  
print(new_libros.head(50))
print('informacion de los libros:')
print(new_libros.info())

# Guardar el DataFrame en un archivo CSV
new_libros.to_csv('ruta_del_archivo.csv', index=False)