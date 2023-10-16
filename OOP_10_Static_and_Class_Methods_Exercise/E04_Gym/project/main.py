from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.gym import Gym
from project.subscription import Subscription
from project.trainer import Trainer

g = Gym()
p = ExercisePlan(1, 1, 10)
g.add_plan(p)
g.add_plan(p)


#
# customer1 = Customer("John", "Maple Street", "john.smith@gmail.com")
# customer2 = Customer("Asen", "Varna", "asen4o@gmail.com")
# customer3 = Customer("Koki", "Trabant Street", "koki_moki@gmail.com")
# equipment = Equipment("Treadmill")
# trainer1 = Trainer("Peter")
# trainer2 = Trainer("Momchil Mashinata")
# trainer3 = Trainer("Kolio Koichev")
# subscription1 = Subscription("14.07.2021", 1, 1, 1)
# subscription2 = Subscription("14.05.2019", 2, 3, 1)
# subscription3 = Subscription("14.05.2023", 3, 2, 1)
# plan1 = ExercisePlan(1, 1, 20)
# plan2 = ExercisePlan(2, 1, 10)
# plan3 = ExercisePlan(3, 1, 30)
# gym = Gym()
# gym.add_customer(customer1)
# gym.add_customer(customer2)
# gym.add_customer(customer3)
# gym.add_equipment(equipment)
# gym.add_trainer(trainer1)
# gym.add_trainer(trainer2)
# gym.add_trainer(trainer3)
# gym.add_plan(plan1)
# gym.add_plan(plan2)
# gym.add_plan(plan3)
# gym.add_subscription(subscription1)
# gym.add_subscription(subscription2)
# gym.add_subscription(subscription3)
# print(Customer.get_next_id())
# print(gym.subscription_info(2))
