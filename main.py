import random
class Cat:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.hunger = 0
        self.alive = True
        self.water = 10
        self.fat = 0
        self.treacherous = 10
    def to_eat(self):
        print("time to eat")
        self.hunger -= 8
        self.gladness += 3
        self.water -= 1
        self.fat += 5
    def to_sleep(self):
        print("time to sleep")
        self.gladness += 7
        self.hunger += 2
        self.water -= 3
        self.treacherous -= 3

    def to_play(self):
        print("time to play")
        self.gladness +=5
        self.hunger += 4
        self.water -= 7
        self.fat -= 7
    def to_drink(self):
        print("time to get drunk")
        self.gladness += 1
        self.hunger -= 0.2
        self.water += 15
    def to_trick(self):
        print("This house needs new hero")
        self.gladness += 10
        self.water -= 5
        self.hunger += 3
        self.treacherous += 8
        self.fat -= 10
    def is_alive(self):
        if self.hunger > 10:
            print("Died from hunger")
            self.alive = False
            print("BAD CAT!!!")
        elif self.gladness < 0:
            print("Depression")
            self.alive = False
            print("BAD CAT!!!")
        elif self.water <0:
            print("Died from thirst")
            self.alive = False
            print("BAD CAT!!!")
        elif self.fat > 7:
            print("U fat, can't move")
            print("BAD CAT!!!")
            self.alive = False
        elif self.treacherous > 30:
            print("U treacherous, u can rule people")
            print("Winner CAT!!!")
            self.alive = False


    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Hunger = {round(self.hunger, 2)}")
        print(f"Water = {self.water}")
        print(f"Fat = {self.fat}")
        print(f"Treacherous = {self.treacherous}")

    def live(self, day):
        day = "Day" + str(day) + 'of'+ self.name+"live"
        print(f"{day:=^50}")
        live_cube = random.randint(1,5)
        if live_cube == 1:
            self.to_trick()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_drink()
        elif live_cube == 4:
            self.to_eat()
        elif live_cube == 5:
            self.to_play()
        self.end_of_day()
        self.is_alive()

nick = Cat(name="Maggot")
for day in range(365):
    if nick.alive==False:
        break
    nick.live(day)
