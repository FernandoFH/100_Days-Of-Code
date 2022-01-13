# def mult(lista):
#    result = 1
#    from i in range(0, len(lista)):
#        result *= lista[i]

# Suma de una lista dada 
def sum(lista):
    result = 0
    for i in lista:
        result += i
    return result

# Multiplicar de una lista dada 
def multi(lista):
    result = lista[0]
    i = 1
    while i in range(1, len(lista)):
        result = result * lista[i]
        i += 1
    return result

# Invertir string
def inversa(string):
    string = string[::-1]
    return string

# Es palindromo
def is_palindromo(string):
    new_string = inversa(string)
    if string == new_string:
        return True
    else:
        return False

# Superposicion de listas
def superposicion(lista1, lista2):
    for elem in lista1:
        if elem in lista2:
            return True

    return False

if __name__ == '__main__':
    #lista = [-1,2,10]    
    #print(multi(lista))

    #string = 'rodar'
    #print(is_palindromo(string))

    lista1 = [1,2,3,4,5]
    lista2 = [7,8,9,1]
    print(superposicion(lista1, lista2))


  #  def palindromo(sentence):
  #    sentence = str(sentence).lower().replace(' ', '')
  # return sentence == sentence[::-1]