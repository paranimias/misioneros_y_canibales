from collections import deque
from pyautogui import click, moveTo
import time


class State:
    def __init__(self, mis, can, boat) -> None:
        self.mis = mis
        self.can = can
        self.boat = boat

    def __eq__(self, other) -> bool:
        if isinstance(other, State):
            return (
                self.mis == other.mis
                and self.can == other.can
                and self.boat == other.boat
            )
        return False

    def __hash__(self):
        return hash((self.mis, self.can, self.boat))


class Agent:
    def __init__(self):
        # lo más sencillo sería iterar toda la lista de 12 posiciones cada vez que vayamos a revisar un screenshot,
        # y sabremos qué posiciones son (fila, columna) del array de pixeles
        # si registramos la (fila, columna) y las colocamos en actual_coordinates,
        self.all_coordinates = [
            # Lado derecho
            (387, 1645),  # Canibal1, fijo
            (470, 1504),  # Canibal2, fijo
            (722, 1645),  # Canibal3, fijo
            (559, 1601),  # Misionero1, fijo
            (790, 1476),  # Misionero2, fijo
            (930, 1637),  # Misionero3, fijo
            # Lado izquierdo
            #   1.
            #     2.
            #   6.  3.
            #     4.
            #   5.
            (380, 365),  # 1.
            (452, 488),  # 2.
            (559, 603),  # 3.
            (623, 454),  # 4.
            (737, 315),  # 5.
<<<<<<< HEAD
            # la posición 6 solo se usa cuando ganamos
            # (),
=======
            (560, 280),  # 6.
>>>>>>> testing
        ]
        self.actual_coordinates = {
            "M": [],
            "C": [],
            "B": (),
        }

        # actual_coordinates = {
        #   "M" : [(fila,columna),(fila,columna),(fila,columna)],
        #   "C" : [(fila,columna),(fila,columna),(fila,columna)]
        #   "B" : (fila,columna)
        # }

        # Usamos el método calculate_initial_state para conseguir el atributo initial_state
        # No se puede dejar como None porque nos da error si la pasamos a calculate_next_steps
        self.initial_state = State(0,0,0)
        self.final_state = State(0, 0, 0)

        # Cuantos van en el bote (misioneros,canibales)
        self.movements = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

        self.unload_coordinates = {
            "L": [(745, 545), (739, 654), (745, 763)],
            "R": [(745, 1045), (739, 1154), (745, 1263)]
        }

    def compute(self, perception):
        time.sleep(2)
<<<<<<< HEAD

        flag = False

        while not flag:
            self.calculate_actual_coordinates(perception)
            self.initial_state = self.calculate_initial_state()
            flag = self.execute_solution()
            if not flag:
                print("Error en ejecucion, volviendo a ejecutar")

        return "^"
=======
        # Lo primero que hacemos es calcular la posición actual
        self.calculate_actual_coordinates(perception)
        
        # Test para saber si los está calculando o no
        print(self.calculate_side("M"))
        print(self.calculate_side("C"))
        print(self.calculate_side("B"))
        # self.initial_state = self.calculate_initial_state()
        # 1. Calculate_actual_state
        # 2. Agregar una flag (while flag)
        return "*"
>>>>>>> testing

    def calculate_side(self, nombre):
#         self.calculate_actual_coordinates(self.all_coordinates)
        if nombre == "B":
            boat_coordinates = self.actual_coordinates["B"]
            if boat_coordinates[1] > 950:
                return boat_coordinates + ("R",)
            else:
                return boat_coordinates + ("L",)

        triplas = []
        for row, column in self.actual_coordinates[nombre]:
            if column > 950:
                triplas.append((row, column, "R"))
            elif column < 950:
                triplas.append((row, column, "L"))
        return triplas

    def validate(self, state: State):
        can_r = state.can
        mis_r = state.mis
        can_l = 3 - can_r
        mis_l = 3 - mis_r

        if can_r < 0 or can_r > 3 or mis_r < 0 or mis_r > 3:
            return False

        if (mis_r < can_r and mis_r > 0) or (mis_l < can_l and mis_l > 0):
            return False

        else:
            return True

    def calculate_actual_coordinates(self, arr):
        self.actual_coordinates = {
            "M": [],
            "C": [],
            "B": (),
        }
        for row, column in self.all_coordinates:
            # Es ese pixel del color de un canibal?
            if tuple(arr[row][column]) == (24, 93, 160):
                self.actual_coordinates["C"].append((row, column))
            # Es del color de un misionero?
            elif tuple(arr[row][column]) == (157, 178, 255):
                self.actual_coordinates["M"].append((row, column))
        # Es menos azul, o sea es café
        if tuple(arr[950][650])[0] < 80:
            self.actual_coordinates["B"] = (950, 650)
        else:
            self.actual_coordinates["B"] = (960, 1191)

    def calculate_initial_state(self) -> State:
        # Calcular el lado del bote
        if self.calculate_side("B")[2] == "R":
            b = 1
        else:
            b = 0
        # Calcular el cuantos canibales están a la derecha
        c = sum(1 for canibal in self.actual_coordinates["C"] if "R" in canibal)
        # Calcular el cuantos misioneros están a la derecha
        m = sum(1 for misionero in self.actual_coordinates["M"] if "R" in misionero)
        # Retornamos un estado
        return State(c, m, b)

    def calculate_nexts_steps(self, state: State):
        children = []
        can_r = state.can
        mis_r = state.mis
        boat = state.boat

        # Sumamos al lado izquierdo y restamos para el lado derecho
        if boat == 1:
            direction = -1
            new_boat = 0
        else:
            direction = 1
            new_boat = 1

        for delta_mis, delta_can in self.movements:
            new_mis = mis_r + (delta_mis * direction)
            new_can = can_r + (delta_can * direction)
            new_state = State(new_mis, new_can, new_boat)

            if self.validate(new_state):
                children.append((new_state, (delta_mis, delta_can)))

        return children

    def find_way(self):
        if self.initial_state is None:
            return None

        orden_queue = deque([(self.initial_state, [(self.initial_state, None)])])
        visited = set([self.initial_state])
        while orden_queue:
            actual_state, way = orden_queue.popleft()

            if actual_state == self.final_state:
                return way

            else:
                for child, action in self.calculate_nexts_steps(actual_state):
                    if child not in visited:
                        visited.add(child)
                        new_way = way + [(child, action)]
                        orden_queue.append((child, new_way))

    def execute_movement(self, action):
        delta_mis, delta_can = action

        boat_y, boat_x, boat_side = self.calculate_side("B")

        mis_can_move = []
        for i in self.calculate_side("M"):
            if boat_side == i[2]:
                mis_can_move.append((i[0], i[1]))

        can_can_move = []  # Canibales que puedo mover can that I can move
        for i in self.calculate_side("C"):
            if boat_side == i[2]:
                can_can_move.append((i[0], i[1]))

        if len(mis_can_move) < delta_mis:
            print("mis_can_move < delta_mis")
            return False

        if len(can_can_move) < delta_can:
            print("can_can_move < delta_can")
            return False

        for i in range(delta_mis):
            y, x = mis_can_move[i]
            moveTo(x,y)
            click()
            time.sleep(0.5)

        for i in range(delta_can):
            y, x = can_can_move[i]
            moveTo(x,y)
            click()
            time.sleep(0.5)

        moveTo(boat_x, boat_y)#Necesita dos clicks no se porque xd
        click()
        time.sleep(1.5)

        destination_side = "L" if boat_side == "R" else "R"
        for y, x in self.unload_coordinates[destination_side]:
            moveTo(x, y)
            click()
            time.sleep(0.1)
        time.sleep(0.5) 
        return True
    def execute_solution(self, env=None) -> bool:
        way = self.find_way()
        if not way:
            return False

        for i in range(1, len(way)):
            
            state, action = way[i]
            if env is not None:
                # Pequeña pausa para asegurar que terminaron las animaciones del juego
                time.sleep(0.5) 
                nueva_captura = env.screenshot()
                self.calculate_actual_coordinates(nueva_captura)

            sucess = self.execute_movement(action)
            time.sleep(0.5)

            if not sucess:
                print("Fallo en los movimientos")
                return False

        return True
<<<<<<< HEAD
=======

>>>>>>> testing
