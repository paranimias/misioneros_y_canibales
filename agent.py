def Agent():
    def __init__(self):
        self.initial_state = (3, 3, 1)
        self.final_state = (0, 0, 0)

    def validate(self, estate):
        can_r, mis_r, boat = estate
        can_l = 3 - can_r
        mis_l = 3 - mis_r

        if can_r < 0 or can_r > 3 or mis_r < 0 or mis_r > 3:
            return False

        if (mis_r < can_r and mis_r > 0) or (mis_l < can_l and mis_l > 0):
            return False

        else:
            return True

    # next_step(self, estate):
