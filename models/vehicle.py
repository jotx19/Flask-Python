# Author: Prabjot Singh
# This file contains the Vehicle class which has Base variable declarations.

class Vehicle:
    """
    Represents a vehicle record with details about its model year, make, engine, fuel consumption, and CO2 emissions.
    """

    def __init__(self, model_year, make, model, vehicle_class, engine_size, cylinders, transmission, fuel_type,
                 city_consumption, highway_consumption, combined_consumption, co2_emissions, co2_rating, smog_rating, id=None):
        """
        Initializes a Vehicle object with the given parameters.      
        :param model_year: The year the vehicle model was made.
        :param make: The manufacturer of the vehicle.
        # Have many more params which referes to header in csv professor.
        """
        self.id = id  
        self.model_year = model_year
        self.make = make
        self.model = model
        self.vehicle_class = vehicle_class
        self.engine_size = engine_size
        self.cylinders = cylinders
        self.transmission = transmission
        self.fuel_type = fuel_type
        self.city_consumption = city_consumption
        self.highway_consumption = highway_consumption
        self.combined_consumption = combined_consumption
        self.co2_emissions = co2_emissions
        self.co2_rating = co2_rating
        self.smog_rating = smog_rating

    def __str__(self):
        """
        Returns a string representation of the Vehicle object.
        """
        return f"{self.model_year} {self.make} {self.model} {self.city_consumption} L/100 km {self.co2_emissions} g/km"
