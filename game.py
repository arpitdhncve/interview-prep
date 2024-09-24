from types import new_class
from dice import Dice
from gamelogs import Gamelogs
from player import Player
import uuid
from board import Board


class Game:

    def __init__(self, player1:Player, player2:Player, board: Board):
        self.id = str(uuid.uuid4())
        self.player1 = player1
        self.player2 = player2
        self.current_position1 = 0
        self.current_position2 = 0
        self.current_turn = player1
        self.winner = None
        self.board = board

    
    def roll_dice(self, player):
        if self.current_turn != player:
            print("Invalid player turn")
        else:
            dice_number = Dice.roll_dice()
            older_position = self.current_position1 if player == self.player1 else self.current_position2
            new_position = dice_number + older_position

            board_response = self.board.get_new_position(new_position)

            print(board_response)

            
            self.update_position(player, board_response["final_position"])
            self.update_turn(player)
            self.update_logs(player, dice_number, older_position, new_position, board_response["encounter_by"], board_response["final_position"])


      
    def update_position(self, player, new_position):
        if player == self.player1:
            self.current_position1 = new_position
        else:
            self.current_position2 = new_position

    def update_turn(self, player):
        self.current_turn = self.player2 if player == self.player1 else self.player1

    
    def update_logs(self, player, dice_number, older_position, position_after_dice, encounter_by, final_position):
        Gamelogs(player, self.id, dice_number, older_position, position_after_dice, encounter_by, final_position)

    

    def get_player_positions(self):
        print(f'player1 position is {self.current_position1} and player2 position is {self.current_position2}')

    
    def get_turn(self):
        print(self.current_turn.email)

       

        



    


    



    