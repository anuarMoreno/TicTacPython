import tic_tac_game, random

while True:

    print("Bienvenido a Tic-Tac-Toe Game by @anuarmeng, ¿Cómo deseas jugar?:\n"
          "1. Jugador vs CPU\n"
          "2. Jugador A vs Jugador B\n"
          "3. Salir\n")

    mode_game = tic_tac_game.select_mode()

    if mode_game == 1:  # Modalidad Jugador vs CPU

        print("Instrucciones:\n"
              "- En este juego llamado tic Tac toe, tu rival será la CPU.\n"
              "- Debes insertar un número del 1 al 9 para seleccionar donde quieres jugar.\n"
              "- Utilizarás la letra O para representar tus movimientos y la CPU la letra X.\n"
              "- ¡Empieza a Jugar!")

        result = False
        tictac_board = [[1,2,3],[4,5,6],[7,8,9]]
        tic_tac_game.print_board(tictac_board)

        while result == False:

            while True:
                try:
                    value = int(input("Ingresa tu movimiento: "))

                    tester = tic_tac_game.free_fields(value, tictac_board)

                    row = tester[0]
                    column = tester[1]
                    checker = tester[2]

                    tic_tac_game.enter_move(row, column, checker, tictac_board)
                    if checker:
                        print("¡Bien Jugado!")
                        tic_tac_game.print_board(tictac_board)
                        break

                except ValueError:
                    print("Ingresa un valor correcto, puedes observarlos en la última jugada.")
                except:
                    print("Ha ocurrido algo extraño, lo lamentamos :(")

            results = tic_tac_game.victory_for(tictac_board,mode_game)
            result = results[0]
            winner = results[1]

            if result:
                print(winner)
                break

            while True:
                value_cpu = int(random.randrange(0,10))

                tester_cpu = tic_tac_game.free_fields(value_cpu,tictac_board)

                row_cpu = tester_cpu[0]
                column_cpu = tester_cpu[1]
                checker_cpu = tester_cpu[2]

                tic_tac_game.enter_cpu_move(row_cpu,column_cpu,checker_cpu,tictac_board)

                if checker_cpu:
                    print("La CPU ha jugado en la casilla",value_cpu,"¡Es tu turno!")
                    tic_tac_game.print_board(tictac_board)
                    break

            results = tic_tac_game.victory_for(tictac_board,mode_game)
            result = results[0]
            winner = results[1]

            if result:
                print(winner)
                break

    elif mode_game == 2:    # Modalidad jugador A vs Jugador B
        print("Instrucciones:\n"
              "- En este modo jugarán 1 vs 1, Jugador A y B.\n"
              "- Deben insertar un número del 1 al 9 para seleccionar donde quieren jugar.\n"
              "- JugadorA utilizará la letra O para representar sus movimientos y JugadorB la letra X.\n"
              "- ¡Empieza el juego!")

        result = False
        tictac_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        tic_tac_game.print_board(tictac_board)

        while result == False:

            while True:
                try:
                    value = int(input("Juagador A, ingresa tu movimiento: "))

                    tester = tic_tac_game.free_fields(value, tictac_board)

                    row = tester[0]
                    column = tester[1]
                    checker = tester[2]

                    tic_tac_game.enter_move(row, column, checker, tictac_board)
                    if checker:
                        print("¡Bien Jugado!")
                        tic_tac_game.print_board(tictac_board)
                        break

                except ValueError:
                    print("Ingresa un valor correcto, puedes observarlos en la última jugada")
                except:
                    print("Ha ocurrido algo extraño, lo lamentamos :(")

            results = tic_tac_game.victory_for(tictac_board,mode_game)
            result = results[0]
            winner = results[1]

            if result:
                print(winner)
                break

            while True:
                try:
                    value2 = int(input("Jugador B, ingresa tu movimiento: "))

                    tester = tic_tac_game.free_fields(value2, tictac_board)

                    row2 = tester[0]
                    column2 = tester[1]
                    checker2 = tester[2]

                    tic_tac_game.enter_move2(row2, column2, checker2, tictac_board)
                    if checker2:
                        print("¡Bien Jugado!")
                        tic_tac_game.print_board(tictac_board)
                        break

                except ValueError:
                    print("Ingresa un valor correcto, puedes observarlos en la última jugada")
                except:
                    print("Ha ocurrido algo extraño, lo lamentamos :(")

            results = tic_tac_game.victory_for(tictac_board,mode_game)
            result = results[0]
            winner = results[1]

            if result:
                print(winner)
                break

    elif mode_game == 3:    # Salir del Juego.
        print("¡Gracias por jugar!, hasta la próxima")
        break