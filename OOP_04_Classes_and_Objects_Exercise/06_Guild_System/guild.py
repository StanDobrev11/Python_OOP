from typing import List


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players: List['class Player'] = []  # [Player('Ivan', 100, 20), ...]

    def assign_player(self, player) -> str:
        if player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        elif player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        else:
            return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str) -> str:
        try:
            player = next(filter(lambda p: p.name == player_name, self.players))
            self.players.remove(player)
            player.guild = "Unaffiliated"
            return f"Player {player_name} has been removed from the guild."
        except StopIteration:
            return f"Player {player_name} is not in the guild."
        # for player in self.players:
        #     if player.name == player_name:
        #         player.guild = "Unaffiliated"
        #         self.players.remove(player)
        #         return f"Player {player_name} has been removed from the guild."
        #     else:
        #         return f"Player {player_name} is not in the guild."

    def guild_info(self) -> str:
        players_data = '\n'.join(player.player_info() for player in self.players)
        return f"Guild: {self.name}\n" + players_data
