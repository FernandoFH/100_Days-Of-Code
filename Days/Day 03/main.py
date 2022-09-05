def suma(x, y):
    '''
    Funcion que suma dos numeros
    Args:
        x (int): Primer numero
        y (int): Segundo numero
    Returns:
        int: Suma de los dos numeros  
    '''
    return x + y

def escribir(fpath, data_in):
    '''
    Funcion que escribe un archivo de texto
    Args:
        fpath (str): Ruta del archivo
        data_in (str): Datos a escribir
    '''
    with open(fpath, 'w') as file_in:
        file_in.write(data_in)

class calculadora:
    def sumar(a, b):
        return suma(a, b)