from game import Game
from player import Player
from board import Board


class SnakeAndLadder:

    @staticmethod
    def run():
        print("In the main file")

        board = Board()

        board.add_snake(12, 4)
        board.add_snake(32, 16)
        board.add_snake(67, 45)
        board.add_snake(75, 54)
        board.add_snake(98, 14)

        board.add_ladder(1,7)
        board.add_ladder(2,8)
        board.add_ladder(3,9)
        board.add_ladder(4,10)
        board.add_ladder(5,11)
        board.add_ladder(6,12)

       
        Player1 = Player("abc@gmail.com")
        Player2 = Player("qwerty@gmail.com")

        game1 = Game( Player1, Player2, board)

        game1.get_turn()

        game1.roll_dice(Player1)

        game1.get_player_positions()

        game1.roll_dice(Player1)

        game1.get_turn()

        game1.roll_dice(Player2)

        game1.get_player_positions()

        game1.roll_dice(Player1)

        game1.get_player_positions()
        




if __name__ == "__main__":
    SnakeAndLadder.run()