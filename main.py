class Car:
    def __init__(self, type, max_speed, name, made_in, company):
        self.type = type
        self.max_speed = max_speed
        self.name = name
        self.made_in = made_in
        self.company = company

    def __str__(self):
        return (f"Car(type='{self.type}', max_speed={self.max_speed}, "
                f"name='{self.name}', made_in='{self.made_in}', "
                f"company='{self.company}')")

my_car = Car(type="Bugatti", max_speed=270, name="Bugatti Chiron Super Sport", made_in="France", company="Bugatti Automobiles S.A.S")
print(my_car)



class Hypercar(Car):
    def __init__(self, type, max_speed, name, made_in, company, zero_to_sixty, price):
      
        super().__init__(type, max_speed, name, made_in, company)
        
       
        self.zero_to_sixty = zero_to_sixty
        self.price = price

    def __str__(self):
        return (f"Car(type='{self.type}', max_speed={self.max_speed}, name='{self.name}', "
                f"made_in='{self.made_in}', company='{self.company}', "
                f"zero_to_sixty='{self.zero_to_sixty}', price='{self.price}')")



my_hypercar = Hypercar(
    type="Bugatti", 
    max_speed=270, 
    name="Bugatti Chiron ", 
    made_in="France", 
    company="Bugatti Automobiles S.A.S",
    zero_to_sixty="2.2 seconds", 
    price="$3.9 Million"
)

print(my_hypercar)

