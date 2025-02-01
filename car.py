from xml.sax.handler import property_declaration_handler

class Car:
    def __init__(self, make=None, color=None, model=0, price=0, year=0):
        self.make = make
        self.color = color
        self.model = model
        self.price = price
        self.year = year

    def drive(self):
        print('My brother is driving', self.make)

    def info(self):
        print('My favorite car is',self.make,'m5',self.model)
    def info2(self):
        print('Popular car in our country is :',self.make,self.color,self.model)
    def show_model(self):
        print('The most expensive car in the world is :',self.make)
    def dream(self):
        print('In the future I wanna buy',self.make,'in',self.color,'color and model is:',self.model)
    def show_price(self):
        print(f"The price of this {self.make} {self.model} is: ${self.price}.")
    def apply_discount(self, discount_percent):
        
        """Applies a discount to the car's price."""
        if self.price:
            discount_amount = (self.price * discount_percent) / 100
            self.price -= discount_amount
            print(f"Discount applied! New price: ${self.price:.2f}")
        else:
            print("Price is not set.")    
