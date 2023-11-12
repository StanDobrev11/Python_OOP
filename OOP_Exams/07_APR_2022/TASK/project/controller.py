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
            self.supplies.reverse()
            self.supplies.remove(sustenance)
            self.supplies.reverse()
        except IndexError:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        return player.replenish_stamina(sustenance)

    def duel(self, first_player_name: str, second_player_name: str):
        player_1 = [p for p in self.players if p.name == first_player_name][0]
        player_2 = [p for p in self.players if p.name == second_player_name][0]

        if player_1.stamina == 0 or player_2.stamina == 0:
            return self.duel_not_possible(player_1, player_2)

        first_attacker = player_1 if player_2 > player_1 else player_2
        second_attacker = player_1 if first_attacker == player_2 else player_2

        winner = None
        if second_attacker.stamina - first_attacker.stamina / 2 <= 0:
            second_attacker.stamina = 0
            winner = first_attacker
        else:
            second_attacker.stamina -= first_attacker.stamina / 2

        if first_attacker.stamina - second_attacker.stamina / 2 <= 0:
            first_attacker.stamina = 0
            winner = second_attacker
        else:
            first_attacker.stamina -= second_attacker.stamina / 2

        if not winner:
            winner = first_attacker if first_attacker > second_attacker else second_attacker

        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - player.age * 2 <= 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2
            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')

    def __str__(self):
        text = '\n'.join([str(player) for player in self.players])
        text += '\n'
        text += '\n'.join(supply.details() for supply in self.supplies)

        return text.strip()

    @staticmethod
    def duel_not_possible(*players):
        text = []
        for player in players:
            if player.stamina == 0:
                text.append(f"Player {player.name} does not have enough stamina.")

        return '\n'.join(text)
