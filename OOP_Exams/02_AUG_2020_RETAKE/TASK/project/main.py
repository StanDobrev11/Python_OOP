from project.rooms.alone_old import AloneOld
from project.rooms.alone_young import AloneYoung
from project.rooms.old_couple import OldCouple
from rooms.young_couple import YoungCouple
from rooms.young_couple_with_children import YoungCoupleWithChildren
from people.child import Child
from everland import Everland

everland = Everland()


def test_one():
    young_single = (AloneYoung('Johny', 10))
    old_single = AloneOld('Me', 10)
    old_couple = OldCouple("Oldees", 200, 120)
    young_couple = YoungCouple("Johnsons", 200, 205)
    child1 = Child(5, 1, 2, 1)
    child2 = Child(3, 2)
    young_couple_with_children = YoungCoupleWithChildren("Peterson", 700, 520, child1, child2)

    everland.add_room(young_couple)
    everland.add_room(young_couple_with_children)
    everland.add_room(young_single)
    everland.add_room(old_single)
    everland.add_room(old_couple)
    print(everland.get_monthly_consumptions())
    print(everland.pay())
    print(everland.status())


if __name__ == "__main__":
    test_one()
