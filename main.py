from car import Car
if __name__ == '__main__':
    car1=Car()
    car1.make='BMW'
    print(car1.model)
    car1.info()

    car1=Car('Mercedes',2002)
    car1.drive()

    car2=Car('Toyota Camry',' model is ', 70)
    car2.info2()

    car3=Car('Kia k7')
    car3.drive()

    car4=Car('Lexus','white ',570)
    car4.dream()


    car6 = Car('Tesla','red','S',price=23500)
    car6.show_price()

    car7 = Car('Rolls Royce')
    car7.show_model()
    car10 = Car("Tesla", "White", "Model S", 79999, 2022)

   
    car10.display_info()

    # Apply a 10% discount
    car10.apply_discount(10)

    # Show new price
    print(f"Updated Price: ${car1.price}")

