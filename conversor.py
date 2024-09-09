import pandas as pd

def isbn_10_a_13(isbn_10):
    """Esta Funcia recibe un ISBN de diez digitos y lo convierte en uno de trece digitos"""
    # Paso 1: Añadir el prefijo '978'
    isbn_base = '978' + isbn_10[:-1]
    
    # Paso 2: Calcular el dígito de control del ISBN-13
    suma = 0
    for i, digito in enumerate(isbn_base):
        if i % 2 == 0:
            suma += int(digito) *1
        else:
            suma += int(digito) * 3
    
    # Paso 3: Calcular el número de control
    control = (10 - (suma % 10)) % 10

    # Combinar los 12 dígitos con el dígito de control
    isbn_13 = isbn_base + str(control)
    
    return isbn_13

# Ejemplo de uso
isbn_10 = "9505371438 "  # Ejemplo de ISBN-10
isbn_13 = isbn_10_a_13(isbn_10)
print(f"ISBN-10: {isbn_10} convertido a ISBN-13: {isbn_13}")




def convertir_isbn(df,columna):
    """
    Convierte los números ISBN de 10 dígitos a 13 dígitos en un DataFrame.

    Parámetros:
    -----------
    df : pandas.DataFrame
    columna : str nombre de la columna

    Returns:
    --------
    pandas.DataFrame
        DataFrame con la columna  actualizada donde los ISBN de 10
        dígitos han sido convertidos a formato de 13 dígitos.
    """
    # Verificamos si el ISBN es válido (no es nulo) y si tiene 10 dígitos
    df[columna] = df[columna].apply(lambda x: isbn_10_a_13(x) if pd.notna(x) and len(x) == 10 and x[:-1].isdigit() else x)
    return df



# Función para convertir ISBN-10 a ISBN-13
def isbn10_to_isbn13(isbn10):
    # Paso 1: Añadir el prefijo "978" y quitar el último dígito (el dígito de control del ISBN-10)
    isbn_base = "978" + isbn10[:-1]
    
    # Paso 2: Calcular el nuevo dígito de control del ISBN-13
    total = 0
    for i, digit in enumerate(isbn_base):
        if i % 2 == 0:
            total += int(digit) * 1  # Dígitos en posición par se multiplican por 1
        else:
            total += int(digit) * 3  # Dígitos en posición impar se multiplican por 3
    
    check_digit = (10 - (total % 10)) % 10  # Cálculo del dígito de control

    # Paso 3: Retornar el ISBN-13 completo
    return isbn_base + str(check_digit)

# Ejemplo de uso
isbn10 = "9505371438"
isbn13 = isbn10_to_isbn13(isbn10)
print(f"ISBN-10: {isbn10} -> ISBN-13: {isbn13}")

