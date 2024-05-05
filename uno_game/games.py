from constants import CARD, COLOR
from cards import Card
class Uno:
    START_CARD_COUNT = 7

    def __init__(self, players: list) -> None:
        self.turn = 0
        self.moves_count = 0
        self.players = players

    def first_move(self) -> bool:
        return self.moves_count == 0

    def get_current_player(self):
        return self.players[self.turn]
    
    def get_next_move(self):
        self.turn += 1
        self.moves_count += 1

    def get_next_player(self):
        self.get_next_move()
        if self.turn == len(self.players):
            self.reset_turn()
        return self.players[self.turn]
        

    def change_color(self, card):
        new_color = input("Enter color for the wild card: ")
        if new_color in COLOR.MAIN_COLORS:
            card_copy = card.copy()
            card_copy.color = new_color
            return card_copy
        else:
            print("Please enter a correct color!")
            return False


    def reset_turn(self) -> None:
        self.turn = 0

    def reconstruct_order(self, action_type) -> None:
        idx = self.turn
        players = self.players

        if action_type == CARD.ACTION_SKIP_BODY:
            players += players[:idx]
            players = players[idx:]
            self.players = players
        elif action_type == CARD.ACTION_REVERSE_BODY:
            left = players[:idx+1] 
            left.reverse() 
            right = players[idx+1:]
            right.reverse()
            self.players = left + right
            