from project.controller import Controller
from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food

c = Controller()
apple = Food("apple", 22)
cheese = Food("cheese")
juice = Drink("orange juice")
water = Drink("water")
first_player = Player('Peter', 15)
second_player = Player('Lilly', 12, 94)
print(c.add_supply(cheese, apple, cheese, apple, juice, water, water))
print(c.add_player(first_player, second_player))
print(c.duel("Peter", "Lilly"))
print(c.add_player(first_player))
print(c.sustain("Lilly", "Drink"))
first_player.stamina = 0
print(c.duel("Peter", "Lilly"))
print(first_player)
print(second_player)
c.next_day()
print(c)
