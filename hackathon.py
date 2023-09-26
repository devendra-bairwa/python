from datetime import datetime

class FoodItem:
    def __init__(self, name, quantity, best_before_date):
        self.name = name
        self.quantity = quantity
        self.best_before_date = datetime.strptime(best_before_date, '%Y-%m-%d')
        self.discounted = False

    def check_quality(self):
        today = datetime.now()
        if today > self.best_before_date:
            print(f"{self.name} has passed its best before date.")
            return False
        else:
            days_left = (self.best_before_date - today).days
            print(f"{self.name} has {days_left} days left until its best before date.")
            return True

    def apply_discount(self):
        self.discounted = True
        print(f"A discount has been applied to {self.name}.")

class Supermarket:
    def __init__(self):
        self.food_items = []

    def add_food_item(self, food_item):
        self.food_items.append(food_item)

    def remove_food_item(self, food_item_name):
        for item in self.food_items:
            if item.name == food_item_name:
                self.food_items.remove(item)
                break

    def display_food_items(self):
        for item in self.food_items:
            print(f"{item.name}: {item.quantity}")

    def stimulate_demand(self):
        for item in self.food_items:
            if not item.check_quality() and not item.discounted:
                item.apply_discount()

class Restaurant(Supermarket):
    def __init__(self):
        super().__init__()
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def notify_customers_of_discounts(self):
        discounted_items = [item for item in self.food_items if item.discounted]
        
if len(discounted_items) > 0:
            message = "Discounts available on: "
            
for item in discounted_items:
                message += f"{item.name}, "
            
for customer in self.customers:
                customer.receive_notification(message)

class Customer:
    def __init__(self, name):
        self.name = name

def receive_notification(self,message):print(f"Dear {self.name}, {message}")

supermarket=Supermarket()
restaurant=Restaurant()

hunger_relief_organization=HungerReliefOrganization()

banana=FoodItem("Banana",10,"2023-03-25")
apple=FoodItem("Apple",5,"2023-04-01")

supermarket.add_food_item(banana)
supermarket.add_food_item(apple)

restaurant.add_food_item(banana)
restaurant.add_food_item(apple)

alice=Customer("Alice")
bob=Customer("Bob")

restaurant.add_customer(alice)
restaurant.add_customer(bob)

print("Supermarket Inventory:")
supermarket.display_food_items()

print("\nRestaurant Inventory:")
restaurant.display_food_items()

print("\nStimulating demand...")
supermarket.stimulate_demand()
restaurant.stimulate_demand()

print("\nNotifying customers of discounts...")
restaurant.notify_customers_of_discounts()