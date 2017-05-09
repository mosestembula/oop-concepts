
""" this OOP program is a simple demostration of how a vehicle dealership 
company that sells cars and can buy them back from will customers
It considers that the vehicles vary from cars, to trucks and then the motorcycle down the line
At this point, the assumption is that each vehicle type has the specified base price. 
With time, this program will be improved to specify indices for particular models in a particular class
"""
from abc import ABCMeta, abstractmethod

class Vehicle(object):
    """A vehicle for sale by moses Car Dealership.


    Attributes:
        wheels: An integer representing the number of wheels the vehicle has.
        miles: The integral number of miles driven on the vehicle.
        make: The make of the vehicle as a string.
        model: The model of the vehicle as a string.
        year: The integral year the vehicle was built.
        sold_on: The date the vehicle was sold.
    """

    __metaclass__ = ABCMeta

    base_sale_price = 0

    # any car can either be bought from the customers or sold to them

    def sale_price(self):

        """Return the sale price for this vehicle as a float amount."""
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 6000.0 * self.wheels

    def purchase_price(self):
        """Return the price for which we would pay to purchase the vehicle."""
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return self.base_sale_price - (.10 * self.miles)

    @abstractmethod
    def vehicle_type():
        """"Return a string representing the type of vehicle this is."""
        pass


class Car(Vehicle):
    """A car for sale by Mosesco Car Dealership."""

    base_sale_price = 8000
    wheels = 4

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'car'

class Truck(Vehicle):
    """A truck for sale by Mosesco Car Dealership."""

    base_sale_price = 25000
    wheels = 4

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'truck'

class LorryTruck(Vehicle):
    """A lorry truck for sale by Mosesco Car Dealership."""

    base_sale_price = 15000
    wheels = 6

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'Lorry truck'
class canterTruck(Vehicle):
    """A lorry truck for sale by Mosesco Car Dealership."""

    base_sale_price = 10000
    wheels = 4

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'canter truck'

class Tuktuk(Vehicle):
    """A Tuktuk for sale by Mosesco Car Dealership."""

    base_sale_price = 5500
    wheels = 3

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'TukTuk'


class Motorcycle(Vehicle):
    """A motorcycle for sale by Mosesco Car Dealership."""

    base_sale_price = 4000
    wheels = 2

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'motorcycle'                