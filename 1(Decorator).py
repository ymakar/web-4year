import sys
sys.stdout.reconfigure(encoding='utf-8')

class Drink:
    def cost(self):
        return 0

class Coffee(Drink):
    def cost(self):
        return 20

class DrinkDecorator(Drink):
    def __init__(self, drink):
        self.drink = drink

    def cost(self):
        return self.drink.cost()

class Milk(DrinkDecorator):
    def cost(self):
        return self.drink.cost() + 5

class Sugar(DrinkDecorator):
    def cost(self):
        return self.drink.cost() + 2

class Whip(DrinkDecorator):
    def cost(self):
        return self.drink.cost() + 7

if __name__ == "__main__":
    drink = Coffee()
    print("Звичайна кава:", drink.cost())

    drink = Milk(drink)
    print("Кава з молоком:", drink.cost())

    drink = Sugar(drink)
    print("Кава з молоком і цукром:", drink.cost())

    drink = Whip(drink)
    print("Кава з молоком, цукром і вершками:", drink.cost()) 
