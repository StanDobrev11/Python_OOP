from OOP_06_Inheritance_Exercise.Players_and_Monsters.project.blade_knight import BladeKnight
from OOP_06_Inheritance_Exercise.Players_and_Monsters.project.elf import Elf
from OOP_06_Inheritance_Exercise.Players_and_Monsters.project.hero import Hero
from OOP_06_Inheritance_Exercise.Players_and_Monsters.project.muse_elf import MuseElf
from OOP_06_Inheritance_Exercise.Players_and_Monsters.project.soul_master import SoulMaster

hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)

bladeknight = BladeKnight('Pinko', 17)
for item in bladeknight.__class__.mro():
    print(item.__name__)
print()
soulmaster = SoulMaster("Master", 233)
for item in soulmaster.__class__.mro():
    print(item.__name__)
print()
museelf = MuseElf('Ive', 20)
for item in museelf.__class__.mro():
    print(item.__name__)
