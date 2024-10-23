# vehicle_files_io.py
# Author: Prabjot Singh
# This class is responsible for handling file input/output operations related to vehicle data in CSV format.

import csv
import os
from models.vehicle import Vehicle

class VehicleFileIO:
    """
    A class to handle file input/output operations for vehicle records stored in a CSV file.
    
    Attributes:
        filename (str): The path to the CSV file containing vehicle data.
    """
    
    def __init__(self, filename):
        """
        Initializes the VehicleFileIO with the specified filename.
        """
        self.filename = filename

    def load_vehicles(self):
        """
        Reads vehicle data from a CSV file and loads it into a list of Vehicle objects.
        """
        vehicles = []
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.DictReader(file)
                for i, row in enumerate(reader):
                    # Create a Vehicle object using data from the CSV row
                    vehicle = Vehicle(
                        model_year=row['Model year'],
                        make=row['Make'],
                        model=row['Model'],
                        vehicle_class=row['Vehicle class'],
                        engine_size=row['Engine size (L)'],
                        cylinders=row['Cylinders'],
                        transmission=row['Transmission'],
                        fuel_type=row['Fuel type'],
                        city_consumption=row['City (L/100 km)'],
                        highway_consumption=row['Highway (L/100 km)'],
                        combined_consumption=row['Combined (L/100 km)'],
                        co2_emissions=row['CO2 emissions (g/km)']
                    )
                    vehicles.append(vehicle)
        except FileNotFoundError:
            # Print an error message if the CSV file is not found
            print(f"Error: The file {self.filename} does not exist.")
        
        return vehicles

    def save_vehicles(self, vehicles):
        """
        Writes vehicle data from a list of Vehicle objects into a CSV file.
        This method overwrites the existing file with updated data.
        """
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Model year', 'Make', 'Model', 'Vehicle class', 'Engine size (L)', 
                             'Cylinders', 'Transmission', 'Fuel type', 
                             'City (L/100 km)', 'Highway (L/100 km)', 
                             'Combined (L/100 km)', 'CO2 emissions (g/km)'])
            for vehicle in vehicles:
                writer.writerow([
                    vehicle.model_year, vehicle.make, vehicle.model, vehicle.vehicle_class,
                    vehicle.engine_size, vehicle.cylinders, vehicle.transmission,
                    vehicle.fuel_type, vehicle.city_consumption, vehicle.highway_consumption,
                    vehicle.combined_consumption, vehicle.co2_emissions
                ])
