from typing import List

from project.player import Player
from project.supply.supply import Supply


class Controller:
    VALID_FOOD = ['Food', 'Drink']

    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *players):  # *players = (player1: Player, player2: Player, ...)
        added = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                added.append(player.name)
        return f"Successfully added: {', '.join(added)}"

    def add_supply(self, *supplies):
        for supply in supplies:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        if sustenance_type not in Controller.VALID_FOOD:
            return

        try:
            player = [p for p in self.players if p.name == player_name][0]
        except IndexError:
            return

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        try:
            sustenance = [sup for sup in self.supplies if sup.type == sustenance_type][-1]
        except IndexError:
            raise Exception(f"There are no {sustenance_type} supplies left!")

        return player.replenish_stamina(sustenance)

    def __str__(self):
        text = '\n'.join([str(player) for player in self.players])
        text += '\n'
        text += '\n'.join(supply.details() for supply in self.supplies)

        return text


