# add_vehicle_test.py

from persistence.vehicleFile import VehicleDBIO
from models.vehicle import Vehicle

def test_add_vehicle():
    # Initialize the DBIO class with database connection details
    vehicle_dbio = VehicleDBIO("localhost", "root", "root", "vehicles")

    # Create a new vehicle object with the test data
    vehicle = Vehicle(
        model_year=2024,
        make="Toyota",
        model="Camry",
        vehicle_class="Sedan",
        engine_size=2.5,
        cylinders=4,
        transmission="Automatic",
        fuel_type="Gasoline",
        city_consumption=8.5,
        highway_consumption=6.0,
        combined_consumption=7.0,
        co2_emissions=140,
        co2_rating="A",
        smog_rating="B"
    )

    # Add the vehicle to the database
    vehicle_dbio.add_vehicle(vehicle)  # Test adding a vehicle

if __name__ == '__main__':
    test_add_vehicle()
