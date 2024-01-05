
def print_board(board):  # Esta función imprime el tablero de tic_tac_toe.
    for i in board:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        for j in i:
            element = str(j)
            if element == 'X':
                print("|   "+"\033[91m"+element+"\033[0m",end="\t") # Se usa código ANSI para los colores de O y X
            elif element == 'O':
                print("|   " + "\033[96m" + element + "\033[0m", end="\t")
            else:
                print("|   "+element, end="\t")
        print("|")
        print("|       |       |       |"+"")
    print("+-------+-------+-------+")


def free_fields(value,board): # Esta función busca si la casilla selccionada es válida
    checker = False           # para realizar un movimiento.
    x = None
    y = None
    for i, row in enumerate(board):
        for j, column in enumerate(row):
            if value == column:
                x = i
                y = j
                checker = True
                break
        if checker:
            break
    return [x,y,checker]


def enter_move(row, column, checker, board):  # Esta función pinta el movimiento con una 'O'
    if checker:
        board[row][column] = 'O'
    else:
        print("Ingresa un movimiento válido, recuerda seleccionar solo las casillas disponibles")

def enter_move2(row, column, checker, board): # Esta función pinta el moviento con una 'X'
    if checker:
        board[row][column] = 'X'
    else:
        print("Ingresa un movimiento válido, recuerda seleccionar solo las casillas disponibles")

def enter_cpu_move(row_cpu, column_cpu, checker_cpu, board): # Esta función es usada para pintar movimientos
    if checker_cpu:                                          # generados por la CPU
        board[row_cpu][column_cpu] = 'X'


def victory_for(board,mode_game): # Esta función es capaz de analizar el tablero e identificar
    signal_win = False            # la victoria o el empate.

    if mode_game == 1:
        cpu_win = "Ha ganado la máquina, !buena suerte para la próxima¡\n"
        user_win = "¡Felicidades, Ganaste!\n"
        tie_game = "¡Ha sido un empate!\n"
    elif mode_game == 2:
        cpu_win = "¡Jugador B ha ganado!\n"
        user_win = "¡Jugador A ha ganado!\n"
        tie_game = "¡Ha sido un empate!\n"
    winner = ""
    for row in board:
        check_list = []
        for column in row:
            check_list += [column]
            if check_list == ['X','X','X']:
                winner = cpu_win
                signal_win = True
                break
            elif check_list == ['O','O','O']:
                winner = user_win
                signal_win = True
                break

    for column in range(len(board)):
        check_list2 = []
        for k in range(3):
            x = board[k][column]
            check_list2 += str(x)
            if check_list2 == ['X','X','X']:
                winner = cpu_win
                signal_win = True
                break
            elif check_list2 == ['O','O','O']:
                winner = user_win
                signal_win = True
                break

    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        winner = cpu_win
        signal_win = True
    elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        winner = user_win
        signal_win = True
    elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        winner = cpu_win
        signal_win = True
    elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        winner = user_win
        signal_win = True

    if signal_win == False:
        tie = True
        for row in board:
            for column in row:
                if column != 'X' and column != 'O':
                    tie = False
        if tie == True:
            signal_win = tie
            winner = tie_game


    return [signal_win,winner]

def select_mode():  # Esta función permite al usuario seleccionar la modalidad de Juego o salir del mismo.
    while True:
        try:
            mode_game = int(input("Ingresa el modo de juego deseado: "))
            if mode_game == 1 or mode_game == 2 or mode_game == 3:
                break
            else:
                print("Ingresa un modo correcto, recuerda 1 o 2")
        except ValueError:
            print("Ingresa un modo correcto, recuerda 1 o 2")
        except:
            print("Algo salió mal, lo sentimos")

    return mode_game
