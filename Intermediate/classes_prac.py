class Car:
    def __init__(self, make, model, miles):
        self.make = make.title();
        self.model = model.title();
        self.miles = int(miles);

    def describe(self):
        return (f"\nThis is a {self.make} {self.model}.\n" 
              f"It has {self.miles} miles.\n");


Honda_S2K = Car("Honda", "S2000", 20000);
Toyota_Supra = Car("Toyota", "Supra Mk4", 4000);
Dodge_Viper = Car("Dodge", "Viper Gen 2", 3000);
Nissan_R34 = Car("Nissan", "R34 Nismo", 3000)

Garage = [Honda_S2K, Toyota_Supra, Dodge_Viper, Nissan_R34];
for car in Garage:
    car = car.describe();
    print(car);
