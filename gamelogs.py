from encounter import Encounter

class Gamelogs:

    def __init__(self, player, game_id, dice_number, older_position, position_after_dice, encounter_by: Encounter, final_position):
        self.player = player
        self.game_id = game_id
        self.dice_number = dice_number
        self.older_position = older_position
        self.position_after_dice = position_after_dice
        self.player_encounter = encounter_by
        self.final_position = final_position
        