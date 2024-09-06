from lectura import leer_csv, validar_calidad
from conversor import convertir_isbn

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

new = convertir_isbn(libros_t2,'isbn')
a = new[new['title'] == 'Circuitos electrónicos :']
print(a)