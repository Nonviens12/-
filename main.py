class Computer:

    def __init__(self, name, pow, ener) :
        self.name = name
        self.power = pow
        self.energy = ener
        print("Разработан новый игровой комп", self.name)

    def uncharging(self, amount) :
        print(f"{self.name} работает")
        self.power -= amount
        if (self.power < 1):
            print(f" БРАТАН ТЫ ЗАПОСТИЛ КРИНЖ {self.name} РАЗРЯЖЕННННН........")

    def info(self):
        print(f"Компуктер - {self.name} - {self.power} - {self.energy}")




ryzen = Computer("Ryzen", 50, 100)
ryzen.uncharging(10)
ryzen.uncharging(10)
ryzen.uncharging(10)
ryzen.uncharging(10)
ryzen.uncharging(10)

ryzen.info()