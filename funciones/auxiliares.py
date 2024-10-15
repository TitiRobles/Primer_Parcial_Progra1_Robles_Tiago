import random
from UTN_Heroes_Dataset.utn_pp import mostrar_matriz_texto_tabla, get_original_matrix

matriz = [

]
matriz_concesionaria = get_original_matrix()
nombre_columnas = ['Indice Garage', 'Marca', 'Modelo', 'Unidades', 'Precio', 'Ganancia']

def iniciar_matriz(matriz: list[list]):
    for i in range(20):
        lista_garage = [i + 1, matriz_concesionaria[0][i], matriz_concesionaria[1][i], matriz_concesionaria[2][i], 
                        matriz_concesionaria[3][i], matriz_concesionaria[4][i]]
        matriz.append(lista_garage)
    mostrar_matriz_texto_tabla(matriz, nombre_columnas)

if __name__ == '__main__':
    iniciar_matriz(matriz)

def validar_opcion(min: int, max: int) -> int:
    numero = input(f"Ingrese un numero entre [{min}:{max}]: ")
    if not numero.isdigit() or min > int(numero) or max < int(numero):
        return validar_opcion(min, max)
    return int(numero)

