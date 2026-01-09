class Inventory:

    def __init__(self, __capacity: int ):
        self.capacity = __capacity
        self.items = []


    def add_item(self, item : str):
        if self.capacity > len(self.items):
            self.items.append(item)
        else:
            return "not enough room in the inventory"


    def get_capacity(self):
        return self.capacity

    def __repr__(self):
        items = ', '.join(self.items)
        capacity_left  = self.capacity - len(self.items)
        return f"Items: {items}.\nCapacity left: {capacity_left}"

