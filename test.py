# Author: Prabjot Singh
# Unit test to validate that a new vehicle is correctly added to the in-memory list of vehicles.

import unittest
from business.vehicle_manager import VehicleManager
from models.vehicle import Vehicle

class TestVehicleManager(unittest.TestCase):
    def setUp(self):
        """
        Set up a VehicleManager instance for testing.
        Initialize with a test file that won't affect the main dataset.
        """
        self.vehicle_manager = VehicleManager('data/my2024-fuel-consumption-ratings.csv')

    def test_add_vehicle(self):
        """
        Test if a new vehicle is correctly added to the in-memory list.
        """
        # Define a new vehicle record
        new_vehicle = Vehicle(
            model_year=2024,
            make="Tesla",
            model="Model S",
            vehicle_class="Electric",
            engine_size="None",
            cylinders=0, 
            transmission="Automatic",
            fuel_type="Electric",
            city_consumption="0",
            highway_consumption="0",
            combined_consumption="0",
            co2_emissions="0"
        )

        # Capture the initial number of vehicles in memory and add data and increment the inital count also
        initial_count = len(self.vehicle_manager.get_all_vehicles())
        self.vehicle_manager.add_vehicle(new_vehicle)
        self.assertEqual(len(self.vehicle_manager.get_all_vehicles()), initial_count + 1)
        self.assertEqual(self.vehicle_manager.get_all_vehicles()[-1], new_vehicle)

if __name__ == '__main__':
    unittest.main()
