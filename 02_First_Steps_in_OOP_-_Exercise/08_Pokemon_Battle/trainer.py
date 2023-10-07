from pokemon import Pokemon
from typing import List


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        self.pokemons.append(pokemon)
        return "Caught " + pokemon.pokemon_details()

    def release_pokemon(self, name: str):
        try:
            pokemon = next(filter(lambda p: p.name == name, self.pokemons))
        except StopIteration:
            return "Pokemon is not caught"

        self.pokemons.remove(pokemon)
        return f"You have released {name}"

        # try:
        #     pokemon = [p for p in self.pokemons if p.name == name][0]
        # except IndexError:
        #     return "Pokemon is not caught"
        #
        # self.pokemons.remove(pokemon)
        # return f"You have released {name}"

        # for pokemon in self.pokemons:
        #     if name == pokemon.name:
        #         self.pokemons.remove(pokemon)
        #         return f"You have released {name}"
        # else:
        #     return "Pokemon is not caught"

    def trainer_data(self):
        data = (f"Pokemon Trainer {self.name}\n"
                f"Pokemon count {len(self.pokemons)}\n")
        for pokemon in self.pokemons:
            data += '- ' + pokemon.pokemon_details() + '\n'
        return data
