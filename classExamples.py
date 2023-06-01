class vehicle():
    def whatAmI(self): print('I am a vehicle')
class cars():
    def __init__(self, name, fuelEfficieny):
        self.name = name
        self.fuelEfficiency = fuelEfficieny
        self.gasPrice = 204 # cents per litre
    
    def gasExpense(self, distance):
        print('driving', distance , 'km will cost',end=' ')
        print(round(self.fuelEfficiency*self.gasPrice*distance/(10**4), 4), 'dollars')

class trucks(cars, vehicle):
    def introduce(self): print(self.name, 'is a truck and costs', 
                              round(self.fuelEfficiency*self.gasPrice*(10**-4), 4), 'dollars per km')
class sportscars(cars, vehicle):
    def introduce(self): print(self.name, 'is a sportscar and costs', 
                              round(self.fuelEfficiency*self.gasPrice*(10**-4), 4), 'dollars per km')

carA = sportscars(input('sportscar name?'), int(input('fuel efficiency in cents per litre?')))
carA.whatAmI()
carA.introduce()
carA.gasExpense(int(input('distance planned to travel?')))

carB = trucks(input('turck name?'), int(input('fuel efficiency in cents per litre?')))
carB.whatAmI()
carB.introduce()
carB.gasExpense(int(input('distance planned to travel?')))