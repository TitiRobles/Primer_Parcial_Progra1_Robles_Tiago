from funciones import (mostrar_menu, validar_opcion, 
                    suma_total_unidades, mostrar_matriz, obtener_minimo)
from UTN_Heroes_Dataset.utn_pp import clear_console

def garage_app(matriz: list[list]) -> None:
    while True:
        mostrar_menu()

        opcion = validar_opcion(1, 9)

        match opcion:
            case 1:
                # El punto 1 y 5 estan resueltos en esta funcion
                mostrar_matriz()
            case 2:
                suma_total_unidades(matriz)
            case 3:
                obtener_minimo(matriz)
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                break
        clear_console()


