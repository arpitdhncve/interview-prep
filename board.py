from typing import final
from encounter import Encounter

class Board:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Board, cls).__new__(cls)
            cls._instance.snakes = {}
            cls._instance.ladders = {}

        return cls._instance

    

    def add_snake(self, snake_head, snake_tail):
        self.snakes[snake_head] = snake_tail

    def add_ladder(self, ladder_bottom, ladder_top):
        self.ladders[ladder_bottom] = ladder_top

    def get_new_position(self, position):
        response = {"final_position": position, "encounter_by": Encounter.NONE}
        if position in self.snakes:
            print(f"Landed on a snake at {position}. Moving down to {self.snakes[position]}")
            response["final_position"] = self.snakes[position]
            response["encounter_by"] = Encounter.SNAKE
            return response
        elif position in self.ladders:
            print(f"Landed on a ladder at {position}. Moving up to {self.ladders[position]}")
            response["final_position"] = self.ladders[position]
            response["encounter_by"] = Encounter.LADDER
            return response

        return response