import random
from UTN_Heroes_Dataset.utn_pp import mostrar_matriz_texto_tabla, get_original_matrix

matriz = [
]
matriz_concesionaria = get_original_matrix()
nombre_columnas = ['Indice Garage', 'Marca', 'Modelo', 'Unidades', 'Precio', 'Ganancia']

def iniciar_matriz(matriz: list[list]) -> list[list]:
    """_summary_ Se encarga de inicializar la matriz

    Args:
        matriz (list[list]): _description_

    Returns:
        list[list]: _description_
    """
    cantidad_columnas = len(matriz)
    
    if cantidad_columnas == 0:
        for i in range(20):
            lista_garage = [i + 1, matriz_concesionaria[0][i], matriz_concesionaria[1][i], matriz_concesionaria[2][i], 
                            matriz_concesionaria[3][i], f"${matriz_concesionaria[2][i] * matriz_concesionaria[3][i]}"]
            matriz.append(lista_garage)
        return matriz

def mostrar_matriz():
    """_summary_ Se encarga de mostrar la matriz
    """
    iniciar_matriz(matriz)
    mostrar_matriz_texto_tabla(matriz, nombre_columnas)


def validar_opcion(min: int, max: int) -> int:
    numero = input(f"Ingrese un numero entre [{min}:{max}]: ")
    if not numero.isdigit() or min > int(numero) or max < int(numero):
        return validar_opcion(min, max)
    return int(numero)

def obtener_minimo(matriz: list[list]):
    num_min = 0
    for i in range(len(matriz)):
        if num_min == 0 or matriz[i][3] < num_min:
            num_min = matriz[i][3]
    print(f"El garage con menos unidades tiene {num_min} unidades")

if __name__ == '__main__':
    valor_min = obtener_minimo(matriz)
    print(valor_min)