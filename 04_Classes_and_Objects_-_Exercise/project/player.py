"""
The Player class should receive a name (string), a hp (int), and a mp (int) upon initialization. The Player also has 2
instance attributes: skills (an empty dictionary that will contain the skills of each player and its mana cost) and a
guild set to "Unaffiliated" by default
The Player class should also have two additional methods:
- add_skill(skill_name, mana_cost)
o Adds the skill and the corresponding mana cost to the dictionary of skills. Returns "Skill
{skill_name} added to the collection of the player {player_name}"
o If the skill is already in the collection, returns "Skill already added"
- player_info()
o Returns the player's information, including their skills, in this format:
"Name: {player_name}
Guild: {guild_name}
HP: {hp}
MP: {mp}
==={skill_name_1} - {skill_mana_cost}
==={skill_name_2} - {skill_mana_cost}
…
==={skill_name_N} - {skill_mana_cost}"
"""
from typing import Dict


class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: Dict[str: int] = {}  # {skill_name: mp_required, ...}
        self.guild: str = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int) -> str:
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        return "Skill already added"

    def player_info(self) -> str:
        skills = '\n'.join(f"==={k} - {v}" for k, v in self.skills.items())
        return f"Name: {self.name}\n" + \
            f"Guild: {self.guild}\n" + \
            f"HP: {self.hp}\n" + \
            f"MP: {self.mp}\n" + \
            f"{skills}"
