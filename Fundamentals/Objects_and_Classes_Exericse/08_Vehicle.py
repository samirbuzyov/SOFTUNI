class Vehicle:
    def __init__(self, type: str, model: str, price: float, owner=None):
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner

    def buy(self, money: int, owner: str):
        if self.owner is not None:
            return "Car already sold"

        if money < self.price:
            return "Sorry, not enough money"

        self.owner = owner
        change = money - self.price
        return f"Successfully bought a {self.type}. Change: {change:.2f}"

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return "Vehicle has no owner"


    def __repr__(self):
        if self.owner is not None:
            model = self.model
            type = self.type
            owner = self.owner
            return f"{model} {type} is owned by: {owner}"
        else:
            model = self.model
            type = self.type
            price = self.price
            return f"{model} {type} is on sale: {price}"