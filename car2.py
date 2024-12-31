class car :
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.__price = 0
    def display_info(self):
        print(f"make:{self.make},model:{self.model}, year:{self.year}")

    def set__price(self,price):
            if price > 0:
                print("errorprice cannot be negative")
            else:
                self.__price = price

    def get_price(self):
            return self.__price

car1 = car("lambrghini","centenario",2016)

car1.display_info()
car1.set__price(200000000)
print(f"car1 price:{car1.get_price()}")