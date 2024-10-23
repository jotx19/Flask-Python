# Author: Prabjot Singh
# This file contains the VehicleManager class which handles in-memory management of vehicle records.

from models.vehicle import Vehicle
from persistence.vehicleFile import VehicleFileIO

class VehicleManager:
    """
    Manages vehicle records in memory, including operations like loading, 
    adding, editing, deleting, and saving vehicle data.
    """
    def __init__(self, filename):
        """
        Initialize the VehicleManager with a filename for CSV data.
        Loads the initial data from the CSV into memory.
        :param filename: The CSV file containing vehicle data.
        """
        self.filename = filename
        self.vehicles = []
        self.load_data()

    def load_data(self):
        """
        Loads vehicle data from the specified CSV file into memory.
        Uses the VehicleFileIO class for file reading operations.
        """
        file_io = VehicleFileIO(self.filename)
        self.vehicles = file_io.load_vehicles()

    def get_all_vehicles(self):
        """
        Returns all vehicle records currently in memory.
        :return: List of vehicle records.
        """
        return self.vehicles

    def add_vehicle(self, vehicle):
        """
        Adds a new vehicle record to the in-memory list.
        :param vehicle: Vehicle object to be added.
        """
        self.vehicles.append(vehicle)

    def edit_vehicle(self, index, vehicle):
        """
        Edits an existing vehicle record at the specified index in memory.
        :param index: The index of the vehicle to edit.
        :param vehicle: The updated Vehicle object.
        """
        if 0 <= index < len(self.vehicles):
            self.vehicles[index] = vehicle

    def delete_vehicle(self, index):
        """
        Deletes a vehicle record from memory at the specified index.
        :param index: The index of the vehicle to delete.
        """
        if 0 <= index < len(self.vehicles):
            self.vehicles.pop(index)

    def get_vehicle(self, index):
        """
        Retrieves a single vehicle record from memory by index. 
        :param index: The index of the vehicle to retrieve.
        :return: The Vehicle object at the given index, or None if index is out of range.
        """
        if 0 <= index < len(self.vehicles):
            return self.vehicles[index]
        return None

    def reload_data(self):
        """
        Reloads the vehicle data from the CSV file, replacing the in-memory data.
        """
        self.load_data()

    def save_data(self, output_filename):
        """
        Saves the current in-memory vehicle data to a new CSV file.
        :param output_filename: The name of the file to save the data to.
        """
        file_io = VehicleFileIO(output_filename)
        file_io.save_vehicles(self.vehicles)
