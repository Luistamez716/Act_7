import time

nodos_explorados = 0

def evaluar_tablero(tablero):
    for fila in range(3):
        if tablero[fila][0] == tablero[fila][1] == tablero[fila][2] and tablero[fila][0] != '':
            return 10 if tablero[fila][0] == 'O' else -10
    for columna in range(3):
        if tablero[0][columna] == tablero[1][columna] == tablero[2][columna] and tablero[0][columna] != '':
            return 10 if tablero[0][columna] == 'O' else -10
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != '':
        return 10 if tablero[0][0] == 'O' else -10
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != '':
        return 10 if tablero[0][2] == 'O' else -10
    return 0


def es_terminal(tablero):
    return evaluar_tablero(tablero) != 0 or not any('' in fila for fila in tablero)


def minimax(tablero, jugador, contador_nodos):
    global nodos_explorados
    nodos_explorados = contador_nodos + 1

    if es_terminal(tablero):
        return evaluar_tablero(tablero)

    if jugador == 'O':
        max_eval = -float('inf')
        for fila in range(3):
            for columna in range(3):
                if tablero[fila][columna] == '':
                    tablero[fila][columna] = jugador
                    eval_actual = minimax(tablero, 'X', nodos_explorados)
                    tablero[fila][columna] = ''
                    max_eval = max(max_eval, eval_actual)
        return max_eval
    else:
        min_eval = float('inf')
        for fila in range(3):
            for columna in range(3):
                if tablero[fila][columna] == '':
                    tablero[fila][columna] = jugador
                    eval_actual = minimax(tablero, 'O', nodos_explorados)
                    tablero[fila][columna] = ''
                    min_eval = min(min_eval, eval_actual)
        return min_eval


def mejor_movimiento(tablero):
    max_eval = -float('inf')
    movimiento = (-1, -1)
    global nodos_explorados
    nodos_explorados = 0
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == '':
                tablero[fila][columna] = 'O'
                eval_actual = minimax(tablero, 'X', 0)
                tablero[fila][columna] = ''
                if eval_actual > max_eval:
                    max_eval = eval_actual
                    movimiento = (fila, columna)
    return movimiento, nodos_explorados


def imprimir_tablero(tablero):
    for fila in tablero:
        print(' | '.join(fila))
        print('---------')

def ganador(tablero):
    valor = evaluar_tablero(tablero)
    if valor == 10:
        return 'O'
    elif valor == -10:
        return 'X'
    else:
        return None

def jugar_tic_tac_toe(tablero, jugador, tiempos, nodos):
    imprimir_tablero(tablero)
    if es_terminal(tablero):
        return tablero

    if jugador == 'O':
        print("Turno de la máquina:")
        start_time = time.time()
        (fila, columna), nodos_explorados = mejor_movimiento(tablero)
        end_time = time.time()
        tiempo_ejecucion = end_time - start_time
        tiempos.append(tiempo_ejecucion)
        nodos.append(nodos_explorados)
        tablero[fila][columna] = jugador
        print(f"Tiempo de ejecución: {tiempo_ejecucion:.4f} segundos")
        print(f"Nodos explorados: {nodos_explorados}")
    else:
        fila, columna = map(int, input("Ingrese la fila y columna (0-2) separadas por espacio: ").split())
        if 0 <= fila <= 2 and 0 <= columna <= 2 and tablero[fila][columna] == '':
            tablero[fila][columna] = jugador
        else:
            print("Movimiento inválido. Intente de nuevo.")
            return jugar_tic_tac_toe(tablero, jugador, tiempos, nodos)
    return jugar_tic_tac_toe(tablero, 'O' if jugador == 'X' else 'X', tiempos, nodos)


import matplotlib.pyplot as plt

if __name__ == "__main__":
    tablero_inicial = [['', '', ''],
                       ['', '', ''],
                       ['', '', '']]
    jugador_inicial = 'X'
    tiempos = []
    nodos = []
    tablero_final = jugar_tic_tac_toe(tablero_inicial, jugador_inicial, tiempos, nodos)
    print("Resultado final:")
    imprimir_tablero(tablero_final)
    ganador_final = ganador(tablero_final)
    if ganador_final:
        print(f"El ganador es {ganador_final}")
    else:
        print("Es un empate")

    movimientos = range(1, len(tiempos) + 1)

    plt.figure()
    plt.boxplot(tiempos)
    plt.title("Boxplot de tiempos de ejecución")
    plt.xlabel("Movimientos")
    plt.ylabel("Tiempo (s)")
    plt.show()

    plt.figure()
    plt.bar(movimientos, tiempos)
    plt.title("Gráfico de barras de tiempos de ejecución")
    plt.xlabel("Movimientos")
    plt.ylabel("Tiempo (s)")
    plt.show()

    plt.figure()
    plt.boxplot(nodos)
    plt.title("Boxplot de nodos explorados")
    plt.xlabel("Movimientos")
    plt.ylabel("Nodos explorados")
    plt.show()

    plt.figure()
    plt.bar(movimientos, nodos)
    plt.title("Gráfico de barras de nodos explorados")
    plt.xlabel("Movimientos")
    plt.ylabel("Nodos explorados")
    plt.show()

    
    






