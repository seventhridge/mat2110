class Pumps:

    def __init__(self, capacity):
        self.tankCapacity = {'Regular': capacity, 'Plus': capacity, 'Premium': capacity}
        self.tankContents = {'Regular': capacity, 'Plus': capacity, 'Premium': capacity}
        self.tankPrice    = {'Regular': 0, 'Plus': 0, 'Premium': 0}

        self.revenue = 0

    def fillTank(self,grade, price):
        self.tankContents[grade] = self.tankCapacity[grade]
        self.tankPrice[grade] = price

    def transaction(self,grade, gallons):
        if self.tankContents[grade] < gallons:
            gallons = self.tankContents[grade]
        self.tankContents[grade] = self.tankContents[grade] - gallons
        self.revenue = self.revenue + self.tankPrice[grade] * gallons

    def getTotalSales(self):
        return self.revenue

    def getRemainingCapacity(self):
        return (self.tankContents['Regular'], self.tankContents['Plus'], self.tankContents['Premium'])

    def resetRevenue(self):
        self.revenue = 0


station1 = Pumps(1000)  # all 3 tanks have 1000 gallons capacity each
station1.fillTank("Regular", 2.13)
station1.fillTank("Plus", 2.23)
station1.fillTank("Premium", 2.33)
station1.transaction("Regular", 10.2)  # A transaction of 18.2 gallons 
station1.transaction("Premium", 22.5)
station1.transaction("Regular", 8.5)


revenue = station1.getTotalSales()
(regular, plus, premium) = station1.getRemainingCapacity()
print("The station made sales of ${:8.2f} and has {:8.2f} gallons in it".format(revenue,regular))
