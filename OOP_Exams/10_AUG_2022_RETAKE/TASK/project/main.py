from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.starter import Starter

if __name__ == '__main__':
    french_toast = Starter("French toast", 6.50, 5)
    hummus_and_avocado_sandwich = Starter("Hummus and Avocado Sandwich", 7.90)
    tortilla_with_beef_and_pork = MainDish("Tortilla with Beef and Pork", 12.50, 12)
    risotto_with_wild_mushrooms = MainDish("Risotto with Wild Mushrooms", 15)
    chocolate_cake_with_mascarpone = Dessert("Chocolate Cake with Mascarpone", 4.60, 17)
    chocolate_and_violets = Dessert("Chocolate and Violets", 5.20)
