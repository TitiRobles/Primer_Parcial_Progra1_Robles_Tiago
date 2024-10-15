from .auxiliares import obtener_minimo, iniciar_matriz, nombre_columnas, mostrar_matriz_texto_tabla

# Calcular la cantidad total de unidades almacenadas entre todos los vehículos de la concesionaria.

def suma_total_unidades(matriz: list[list]) -> int:
    """_summary_ Suma el total de todos los vehiculos de la concesionaria

    Args:
        matriz (list[list]): _description_

    Returns:
        int: _description_
    """
    total_unidades = 0
    for i in range(len(matriz)):
        total_unidades += matriz[i][3]
    print(f"El total de unidades almacenadas es {total_unidades}")
    return total_unidades

