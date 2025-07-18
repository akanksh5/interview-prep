from enum import Enum

class Size(Enum):
    SMALL = ('Small',5.0)
    MEDIUM = ('Medium',7.0)
    LARGE =  ('LARGE',10.0)

    def __init__(self,label:str, price: float):
        self.label = label
        self.price = price

class Topping:
    def __init__(self,name:str, cost: float):
        self.name = name
        self.cost = cost

class Crust(Enum):
    CHEESY = ('Cheesy',7.0)
    MAYO = ('Mayo',10.0)
    THIN = ('Thin',11.0)
    
    def __init__(self,crust_type: str, crust_price: float):
        self.crust_type = crust_type
        self.crust_price = crust_price

class Pizza:
    def __init__(self,crust: Crust, size: Size):
        self.size = size
        self.crust = crust
        self.toppings = []

    def add_topping(self,topping):
        self.toppings.append(topping)
    
    def calculate_price(self):
        base_price = self.crust.crust_price + self.size.price
        for topping in self.toppings:
            base_price += topping.cost
        return base_price

class PizzaOrder:
    def __init__(self):
        self.pizzas = []
    
    def add_pizza(self,pizza):
        self.pizzas.append(pizza)
    
    def calculate_total(self):
        total = 0
        for pizza in self.pizzas:
            total += pizza.calculate_price()
        return total
    
mushrooms = Topping('Mushroom',7.0)
capsicum = Topping('Capsicum',3.0)

pizza1 = Pizza(Crust.CHEESY,Size.MEDIUM)
pizza2 = Pizza(Crust.THIN,Size.SMALL)

pizza1.add_topping(mushrooms)
pizza2.add_topping(capsicum)

pizza_order = PizzaOrder()
pizza_order.add_pizza(pizza1)
pizza_order.add_pizza(pizza2)
print(f"Total price of the order is {pizza_order.calculate_total()}")