class ParkTicket:
    def __init__(self, child=False, weekend=False):
        self.price = 100
        if weekend:
            self.inc = 1.2
        else:
            self.inc = 1
        if child:
            self.discount = 0.5
        else:
            self.discount = 1

    def calc_price(self, num):
        return(self.price * self.inc * self.discount * num)

adult = ParkTicket()
kid = ParkTicket(child=True)
print(adult.calc_price(2)+kid.calc_price(1))