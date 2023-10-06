class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        self.pokemons.append(pokemon)
        return "Caught " + pokemon.pokemon_details()

    def release_pokemon(self, name: str):
        for pokemon in self.pokemons:
            if name == pokemon.name:
                self.pokemons.remove(pokemon)
                return f"You have released {name}"
        else:
            return "Pokemon is not caught"

    def trainer_data(self):
        data = (f"Pokemon Trainer {self.name}\n"
                f"Pokemon count {len(self.pokemons)}\n")
        for pokemon in self.pokemons:
            data += '- ' + pokemon.pokemon_details() + '\n'
        return data
