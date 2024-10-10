
class Coffee:

    def cost(self):
        return 5
    
    def ingredients(self):
        return "Coffee"


class CoffeeDecorator(Coffee):

    def __init__(self, coffee):
        self._coffee = coffee

    
    def cost(self):
        return self._coffee.cost()

    def ingredients(self):
        return self._coffee.ingredients()



class withMilk(CoffeeDecorator):

    def cost(self):
        return self._coffee.cost() + 2

    def ingredients(self):
        return self._coffee.ingredients() + "Milk"