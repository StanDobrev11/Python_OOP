from guild import Guild
from player import Player

if __name__ == "__main__":
    player_1 = Player("George", 50, 100)
    player_2 = Player("Ivan", 150, 70)
    print(player_1.add_skill("Shield Break", 20))
    print(player_1.add_skill("Armor", 30))
    # print(player_1.player_info())
    print(player_2.add_skill("Hit-like-a-pro", 40))
    print(player_2.add_skill("Suck-it", 40))
    # print(player_1.player_info())
    guild = Guild("UGT")
    print(guild.assign_player(player_1))
    print(guild.assign_player(player_2))
    print(guild.guild_info())
    # player = Player("George", 50, 100)
    # print(player.add_skill("Shield Break", 20))
    # print(player.player_info())
    # guild = Guild("UGT")
    # print(guild.assign_player(player))
    # print(guild.guild_info())
