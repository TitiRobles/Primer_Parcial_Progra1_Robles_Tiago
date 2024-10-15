from funciones import iniciar_matriz, mostrar_menu, validar_opcion
from UTN_Heroes_Dataset.utn_pp import clear_console

def garage_app(matriz: list[list]) -> None:
    while True:
        mostrar_menu()

        opcion = validar_opcion(1, 9)

        match opcion:
            case 1:
                iniciar_matriz(matriz)
            case 2:
                pass
            case 3:
                pass
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


