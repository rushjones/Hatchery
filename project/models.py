class ParkingLot(models.Model)
    Parkingspace = models.ForeignKey('Parkingspace')
        def __init__(self, Spaces=[0,100], Section=[a,b,c,d,e,], SpaceNumber=[0$
#...

Class Car(models.Model):
        Car = models.ForeignKey('Car')
    def __init__(self, make, model, year):


