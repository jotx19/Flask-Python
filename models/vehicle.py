# Author: Prabjot Singh
# This file contains the Vehicle class, representing a vehicle record with attributes like model year, make, model, fuel consumption, and CO2 emissions.

class Vehicle:
    """
    Represents a vehicle record with details about its model year, make, engine, fuel consumption, and CO2 emissions.
    """
    def __init__(self, model_year, make, model, vehicle_class, engine_size, cylinders, transmission, fuel_type,
                 city_consumption, highway_consumption, combined_consumption, co2_emissions):
        """
        Initializes a Vehicle object with the given parameters.
        
        :param model_year: The year the vehicle model was made.
        :param make: The manufacturer of the vehicle.
        In genral, variable names elaborates its functionality, so
        not overwriting the docs
        """
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

    def __str__(self):
        """
        Returns a string representation of the Vehicle object.
        :return: A string containing the vehicle's model year, make, model, city fuel consumption, and CO2 emissions.
        """
        return f"{self.model_year} {self.make} {self.model} {self.city_consumption} L/100 km {self.co2_emissions} g/km"
