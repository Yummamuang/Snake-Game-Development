import re
from Snake import SnakeClass
import random

class Snake1(SnakeClass):

    def __init__(self):
        super().__init__()
        self.set_name('TEAM Khee Kai Deun 1')  # <--- define team's name here
        self.visited_path = []

    def get_visited_path(self) -> list:
        return self.visited_path

    def add_visited_path(self, step: list):
        self.visited_path.insert(0, step)

    def avoid(self, m):
        # avoid danger zone

        if self.get_position()[0] - 10 < self._SnakeClass__safe_zone_min_x:
            m[0] = 'no'
                
        if self.get_position()[0] + 10 > self._SnakeClass__safe_zone_max_x - 10:
            m[1] = 'no'

        if self.get_position()[1] - 10 < self._SnakeClass__safe_zone_min_y:
            m[2] = 'no'

        if self.get_position()[1] + 10 > self._SnakeClass__safe_zone_max_y - 10:
            m[3] = 'no'

        # avoid artifact
        if self.get_position()[0] - 10 == self.get_artifact_position()[0] and self.get_position()[1] == \
                self.get_artifact_position()[1]:
            m[0] = 'no'

        if self.get_position()[0] + 10 == self.get_artifact_position()[0] and self.get_position()[1] == \
                self.get_artifact_position()[1]:
            m[1] = 'no'

        if self.get_position()[0] == self.get_artifact_position()[0] and self.get_position()[1] - 10 == \
                self.get_artifact_position()[1]:
            m[2] = 'no'

        if self.get_position()[0] == self.get_artifact_position()[0] and self.get_position()[1] + 10 == \
                self.get_artifact_position()[1]:
            m[3] = 'no'

        # avoid self touching
        for block in self.get_body()[1:]:
            for i in range(10, 11, 10):
                if self.get_position()[0] - i == block[0] and self.get_position()[1] == block[1]:
                    m[0] = 'no'

                if self.get_position()[0] + i == block[0] and self.get_position()[1] == block[1]:
                    m[1] = 'no'

                if self.get_position()[0] == block[0] and self.get_position()[1] - i == block[1]:
                    m[2] = 'no'

                if self.get_position()[0] == block[0] and self.get_position()[1] + i == block[1]:
                    m[3] = 'no'

        for block in self.get_enemy_body():
            if self.get_position()[0] - 10 == block[0] and self.get_position()[1] == block[1]:
                m[0] = 'no'

            if self.get_position()[0] + 10 == block[0] and self.get_position()[1] == block[1]:
                m[1] = 'no'

            if self.get_position()[0] == block[0] and self.get_position()[1] - 10 == block[1]:
                m[2] = 'no'

            if self.get_position()[0] == block[0] and self.get_position()[1] + 10 == block[1]:
                m[3] = 'no'
    # override control method here

    def snake_control(self):
        # movement: up, down, left, right

        # self.left()

        if self.get_position() != self.get_fruit_position():
            # rand_case = random.randint(0, 1)
            m = ['ok', 'ok', 'ok', 'ok']
            special = False
            self.avoid(m)


# -------------------------------------------
            if m.count('ok') == 1:
                if m[0] == 'ok':
                    self.left()
                    self.add_visited_path(self.get_position())
                    return 0
                elif m[1] == 'ok':
                    self.right()
                    self.add_visited_path(self.get_position())
                    return 0
                elif m[2] == 'ok':
                    self.up()
                    self.add_visited_path(self.get_position())
                    return 0
                elif m[3] == 'ok':
                    self.down()
                    self.add_visited_path(self.get_position())
                    return 0

            if m.count('ok') < 4 and len(self.get_body()) > 20:
                for block in self.get_body()[1:]:
                    bo = ['ok', 'ok', 'ok', 'ok']
                    for i in range(10, 100, 10):
                        if self.get_position()[0] - i == block[0] and self.get_position()[1] == block[1]:
                            bo[0] = 'no'

                        if self.get_position()[0] + i == block[0] and self.get_position()[1] == block[1]:
                            bo[1] = 'no'

                        if self.get_position()[0] == block[0] and self.get_position()[1] - i == block[1]:
                            bo[2] = 'no'

                        if self.get_position()[0] == block[0] and self.get_position()[1] + i == block[1]:
                            bo[3] = 'no'
                    if m[0] == 'ok' and m[1] == 'ok':
                        if bo[0] == 'no':
                            self.right()
                            self.add_visited_path(self.get_position())
                            return 0
                        elif bo[1] == 'no':
                            self.left()
                            self.add_visited_path(self.get_position())
                            return 0
                    elif m[2] == 'ok' and m[3] == 'ok':
                        if bo[2] == 'no':
                            self.down()
                            self.add_visited_path(self.get_position())
                            return 0
                        elif bo[3] == 'no':
                            self.up()
                            self.add_visited_path(self.get_position())
                            return 0
                    elif m[1] == 'ok' and m[3] == 'ok':
                        if bo[1] == 'ok':
                            self.right()
                            self.add_visited_path(self.get_position())
                            return 0
                        elif bo[3] == 'ok':
                            self.down()
                            self.add_visited_path(self.get_position())
                            return 0
                    elif m[0] == 'ok' and m[2] == 'ok':
                        if bo[0] == 'ok':
                            self.left()
                            self.add_visited_path(self.get_position())
                            return 0
                        elif bo[2] == 'ok':
                            self.up()
                            self.add_visited_path(self.get_position())
                            return 0
                    elif m[0] == 'ok' and m[3] == 'ok':
                        if bo[0] == 'ok':
                            self.left()
                            self.add_visited_path(self.get_position())
                            return 0
                        elif bo[3] == 'ok':
                            self.up()
                            self.add_visited_path(self.get_position())
                            return 0
                    else:
                        ready_move = []

                        if m[0] == 'ok':
                            ready_move.append('ml')
                        if m[1] == 'ok':
                            ready_move.append('mr')
                        if m[2] == 'ok':
                            ready_move.append('mu')
                        if m[3] == 'ok':
                            ready_move.append('md')

                        ready_move_len = len(ready_move)
                        rand_idx = 0
                        if ready_move_len > 1:
                            rand_idx = random.randint(0, ready_move_len - 1)

                        if ready_move_len > 0:
                            if ready_move[rand_idx] == 'ml' and m[1] == 'ok':
                                self.left()
                                self.add_visited_path(self.get_position())
                            elif ready_move[rand_idx] == 'mr' and m[1] == 'ok':
                                self.right()
                                self.add_visited_path(self.get_position())
                            elif ready_move[rand_idx] == 'mu' and m[2] == 'ok':
                                self.up()
                                self.add_visited_path(self.get_position())
                            elif ready_move[rand_idx] == 'md' and m[3] == 'ok':
                                self.down()
                                self.add_visited_path(self.get_position())
                            return 0

            for block in self.get_enemy_body():
                if self.get_position()[0] - 10 == block[0] and self.get_position()[1] == block[1]:
                    if m[2] == 'no':
                        self.down()
                        self.add_visited_path(self.get_position())
                    else:
                        self.up()
                        self.add_visited_path(self.get_position())
                    return 0

                elif self.get_position()[0] + 10 == block[0] and self.get_position()[1] == block[1]:
                    if m[2] == 'no':
                        self.down()
                        self.add_visited_path(self.get_position())
                    else:
                        self.up()
                        self.add_visited_path(self.get_position())
                    return 0

                elif self.get_position()[0] == block[0] and self.get_position()[1] - 10 == block[1]:
                    if m[0] == 'no':
                        self.right()
                        self.add_visited_path(self.get_position())
                    else:
                        self.left()
                        self.add_visited_path(self.get_position())
                    return 0

                elif self.get_position()[0] == block[0] and self.get_position()[1] + 10 == block[1]:
                    if m[0] == 'no':
                        self.right()
                        self.add_visited_path(self.get_position())
                    else:
                        self.left()
                        self.add_visited_path(self.get_position())
                    return 0


# ---------------------------------------

            if self.get_position()[0] > self.get_fruit_position()[0] and m[0] == 'ok':
                self.left()
                self.add_visited_path(self.get_position())
            elif self.get_position()[0] < self.get_fruit_position()[0] and m[1] == 'ok':
                self.right()
                self.add_visited_path(self.get_position())
            elif self.get_position()[1] < self.get_fruit_position()[1] and m[3] == 'ok':
                self.down()
                self.add_visited_path(self.get_position())
            elif self.get_position()[1] > self.get_fruit_position()[1] and m[2] == 'ok':
                self.up()
                self.add_visited_path(self.get_position())
            else:
                ready_move = []

                if m[0] == 'ok':
                    ready_move.append('ml')
                if m[1] == 'ok':
                    ready_move.append('mr')
                if m[2] == 'ok':
                    ready_move.append('mu')
                if m[3] == 'ok':
                    ready_move.append('md')

                ready_move_len = len(ready_move)
                rand_idx = 0
                if ready_move_len > 1:
                    rand_idx = random.randint(0, ready_move_len - 1)

                if ready_move_len > 0:
                    if ready_move[rand_idx] == 'ml' and m[1] == 'ok':
                        self.left()
                        self.add_visited_path(self.get_position())
                    elif ready_move[rand_idx] == 'mr' and m[1] == 'ok':
                        self.right()
                        self.add_visited_path(self.get_position())
                    elif ready_move[rand_idx] == 'mu' and m[2] == 'ok':
                        self.up()
                        self.add_visited_path(self.get_position())
                    elif ready_move[rand_idx] == 'md' and m[3] == 'ok':
                        self.down()
                        self.add_visited_path(self.get_position())
                    return 0
        else:
            ready_move = []

            if m[0] == 'ok':
                ready_move.append('ml')
            if m[1] == 'ok':
                ready_move.append('mr')
            if m[2] == 'ok':
                ready_move.append('mu')
            if m[3] == 'ok':
                ready_move.append('md')

            ready_move_len = len(ready_move)
            rand_idx = 0
            if ready_move_len > 1:
                rand_idx = random.randint(0, ready_move_len - 1)

            if ready_move_len > 0:
                if ready_move[rand_idx] == 'ml' and m[1] == 'ok':
                    self.left()
                    self.add_visited_path(self.get_position())
                elif ready_move[rand_idx] == 'mr' and m[1] == 'ok':
                    self.right()
                    self.add_visited_path(self.get_position())
                elif ready_move[rand_idx] == 'mu' and m[2] == 'ok':
                    self.up()
                    self.add_visited_path(self.get_position())
                elif ready_move[rand_idx] == 'md' and m[3] == 'ok':
                    self.down()
                    self.add_visited_path(self.get_position())
                return 0