from vehicle import Vehicle
from engine import Engine


class Car(Vehicle):
    def __init__(self, num_of_doors: int, max_speed: int, current_gear: int,
                 model, year, color, price, weight, num_wheels,
                 engine: Engine):
        super().__init__(model, year, color, price, weight, num_wheels)
        self.num_of_doors = num_of_doors
        self.max_speed = max_speed
        self.current_gear = current_gear
#       composition
        self.engine = engine
        self.door_lock = None

    def get_price(self):
        print(f"{self.model} : {self.year} : {self.price}")

    # composition (using method of engine class)
    def start_engine(self):
        self.engine.start()
        print(f"Your {self} is ready to go!")

    def lock_doors(self):
        self.door_lock = True
        print(f"{self}'s doors are locked!")

    def unlock_doors(self):
        self.door_lock = False
        print(f"{self}'s doors are unlocked!")

    def change_gears(self, final_gear: int):
        self.current_gear = final_gear
        print(f"Your current gear is {self.current_gear}")

#   polymorphism (defining methods in child class)
    def start(self):
        print("Insert key, turn ignition, and press gas pedal to start.")

    def stop(self):
        print("Put car in park, turn off ignition, and remove key.")

#   overriding abstract method
    def get_num_wheels(self):
        print("I have four wheels!")
