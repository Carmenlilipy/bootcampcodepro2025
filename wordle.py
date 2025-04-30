# definir la palabra a encontrar, intentos, cantidad de letras
palabra_a_encontrar = "virus"
cantidad_de_letras = 5
intentos = 6

# comparar las palabras( posicion correcta, si existe o no existe en la palabra)
def verificar_palabra_ingresada(palabra_a_encontrar, palabra_ingresada):

# definir una lista y agregar las letras verificadas
 resultado = [] 

 for posicion in range(cantidad_de_letras):
    las_letras_son_iguales = palabra_a_encontrar[posicion] == palabra_ingresada[posicion]

    la_letra_existe = palabra_ingresada[posicion] in palabra_a_encontrar

    if las_letras_son_iguales:
      # agregar las letras entre corchetes
     resultado.append('[' +palabra_ingresada[posicion]+']')
    elif la_letra_existe:
       resultado.append('('+palabra_ingresada[posicion]+')')
    else: 
       resultado.append(palabra_ingresada[posicion])

 return resultado

# hacer la grilla
def imprimir_grilla(grilla):
    cantidad_de_filas = len(grilla)

    for fila in range(cantidad_de_filas):
        print(grilla[fila])

grilla = []

# bienvenida al wordle
print("bienvenido a Wordle")

# restar cantidad de intetos
while intentos > 0:
    print(f"te quedan {intentos}")
    palabra_ingresada = input("Ingrese la Palabra")
    

    if len(palabra_ingresada) != cantidad_de_letras:
        print(f"ingrese una palabra con {cantidad_de_letras} letras")
        continue 
    else:

# verificamos las palabras
     linea_verificada = verificar_palabra_ingresada(palabra_a_encontrar, palabra_ingresada)
    grilla.append(linea_verificada)

    intentos = intentos - 1
    imprimir_grilla(grilla)
    if palabra_ingresada == palabra_a_encontrar:
        print("GANASTEEE")
        break
