"""
    Escribir funciones que dada una cadena y un caracter:
        
        a) Inserte el caracter entre cada letra de la cadena. Ej: 'separar' y ',' debería devolver
        's,e,p,a,r,a,r'
        
        b) Reemplace todos los espacios por el caracter. Ej: 'mi archivo de texto.txt' y '_'
        debería devolver 'mi_archivo_de_texto.txt'
        
        c) Reemplace todos los dígitos en la cadena por el caracter. Ej: 'su clave es: 1540' y
        'X' debería devolver 'su clave es: XXXX'
        
        d) Inserte el caracter cada 3 dígitos en la cadena. Ej. '2552552550' y '.' debería devolver
        '255.255.255.0'
"""

def insertar_caracter(cadena,caracter):
    # Inserte el caracter entre cada letra de la cadena. Ej: 'separar' y ',' debería devolver 's,e,p,a,r,a,r'
        
    for i in range(len(cadena)):
        print(cadena[i],end="")

        if i<=(len(cadena)-2):
            print(caracter,end="")
    print()        

# insertar_caracter("separar",",")
# insertar_caracter("Hola Mundo","@")


def reemplazar_espacio_en_cadena(cadena,caracter):
    # Reemplace todos los espacios por el caracter. Ej: 'mi archivo de texto.txt' y '_' debería devolver 'mi_archivo_de_texto.txt'

    longintud = len(cadena)

    print(f"Cadena: {cadena}")
    
    for i in range(longintud):

        if cadena[i]==" ":
            print(caracter,end="")
        else:
            print(cadena[i],end="")

# reemplazar_espacio_en_cadena("mi archivo de texto.txt","_")



def reemplazar_digitos_en_cadena_por_caracter(cadena,caracter):
    # Reemplace todos los dígitos en la cadena por el caracter. Ej: 'su clave es: 1540' y 'X' debería devolver 'su clave es: XXXX'

    longintud = len(cadena)

    print(cadena)

    for i in range(longintud):

        if (cadena[i]>='0' and cadena[i]<='9'):
            print(caracter,end="")
        else:
            print(cadena[i],end="")
    print()

# reemplazar_digitos_en_cadena_por_caracter("Su clave es: 1234","X")
# reemplazar_digitos_en_cadena_por_caracter("Mi númeor de telefono es 1558384705","-")


def insertar_caracter_cada_tres_digitos(cadena,caracter):
    # Inserte el caracter cada 3 dígitos en la cadena. Ej. '2552552550' y '.' debería devolver '255.255.255.0'

    longintud = len(cadena)

    print(f"Cadena: {cadena}")

    for i in range(longintud):

        if i%3==0 and i!=0:
            print(caracter,end="")
        
        print(cadena[i],end="")
        
    print()


insertar_caracter_cada_tres_digitos("2552552550",".")