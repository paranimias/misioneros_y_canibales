from collections import deque
import numpy as np


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
        self.initial_state = State(3, 3, 1)
        self.final_state = State(0, 0, 0)
        self.actual_state = State(3, 3, 1)

        # Cuantos van en el bote (misioneros,canibales)
        self.movements = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

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

    def calculate_actual_state(self) -> State:
        return State(0, 0, 0)

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
        orden_queue = deque([(self.initial_state, [])])
        visited = set([self.initial_state])

        while orden_queue:
            actual_state, way = orden_queue.popleft()
            if actual_state == self.final_state:
                way.append(actual_state)
                return way
            else:
                for child, actions in self.calculate_nexts_steps(actual_state):
                    if child not in visited:
                        visited.add(child)
                        new_way = way + [actual_state]
                        orden_queue.append((child, new_way))
