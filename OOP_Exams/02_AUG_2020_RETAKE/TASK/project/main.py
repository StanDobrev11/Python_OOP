from everland import Everland
from rooms.alone_young import AloneYoung

from people.child import Child
from rooms.alone_old import AloneOld
from rooms.old_couple import OldCouple

from rooms.young_couple import YoungCouple

from rooms.young_couple_with_children import YoungCoupleWithChildren
from rooms.room import Room

everland = Everland()


def test_one():
    random_room = Room('Random', 200, 4)
    young_single = (AloneYoung('YoungSingle', 10))
    old_single = AloneOld('OldSingle', 10)
    old_couple = OldCouple("OldCouple", 200, 120)
    young_couple = YoungCouple("YoungCouple", 200, 205)
    child1 = Child(5, 1, 2, 1)
    child2 = Child(3, 2)
    young_couple_with_children = YoungCoupleWithChildren("WithChildren", 700, 520, child1, child2)
    everland.add_room(random_room)
    everland.add_room(young_couple) # 2
    everland.add_room(young_couple_with_children) # 4
    everland.add_room(young_single) # 1
    everland.add_room(old_single) # 1
    everland.add_room(old_couple) # 2
    print(everland.get_monthly_consumptions())
    # print()
    print(everland.pay())
    # print()
    print(everland.status())
    # print()
    print(everland.pay())
    # print()
    print(everland.get_monthly_consumptions())
    # print()
    print(everland.status())
    # print()
# from rooms.young_couple import YoungCouple
# from rooms.young_couple_with_children import YoungCoupleWithChildren
# from people.child import Child
# from everland import Everland
#
# everland = Everland()
#
# def test_one():
#     young_couple = YoungCouple("Johnsons", 150, 205)
#
#     child1 = Child(5, 1, 2, 1)
#     child2 = Child(3, 2)
#     young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)
#
#     everland.add_room(young_couple)
#     everland.add_room(young_couple_with_children)
#
#     print(everland.get_monthly_consumptions())
#     print(everland.pay())
#     print(everland.status())


if __name__ == "__main__":
    test_one()
