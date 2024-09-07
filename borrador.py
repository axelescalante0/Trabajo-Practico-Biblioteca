
isbn_na = new_libros[new_libros['isbn'].isna()]

print(isbn_na.info())

titulo_autor_na = isbn_na.groupby(['title', 'author']).size().reset_index(name='count')
print(titulo_autor_na.info())


libros_biblioteca_sin_na = new_libros.dropna(subset=['isbn'])


# Hacer un merge entre 'titulo_autor_na' y 'libros_biblioteca_sin_na' basado en 'title' y 'author'
coincidencias = pd.merge(titulo_autor_na, libros_biblioteca_sin_na, on=['title', 'author'], how='inner')

# Eliminar las filas del DataFrame 'titulo_autor_na' que tienen coincidencias
titulo_autor_na_sin_duplicados = titulo_autor_na[~titulo_autor_na[['title', 'author']].apply(tuple, axis=1).isin(coincidencias[['title', 'author']].apply(tuple, axis=1))]

print(coincidencias.info())