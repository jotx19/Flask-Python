from models.vehicle import Vehicle
from data.db import DB

class VehicleManager:
    """
    Manages vehicle records in a MySQL database, including operations like loading,
    adding, editing, deleting, and saving vehicle data.
    """

    def __init__(self, db_host, db_user, db_password, db_name="vehicles"):
        """
        Initialize the VehicleManager with database connection details and fetch
        the initial list of vehicles.
        """
        self.db = DB(db_host, db_user, db_password, db_name)
        self.db.connect()
        self.vehicles = []  
        self.reload_vehicles()  

    def _execute_query(self, query, params=None):
        """Helper method to execute a query and handle errors."""
        try:
            self.db.execute_query(query, params or ())
        except Exception as e:
            print(f"Error executing query: {e}")
            raise  

    def _fetch_results(self, query, params=None):
        """Helper method to fetch results from a query."""
        try:
            return self.db.fetch_results(query, params or ())
        except Exception as e:
            print(f"Error fetching results: {e}")
            raise  

    def get_all_vehicles(self):
        """Returns the list of vehicle objects (updated after calling reload_vehicles)."""
        return self.vehicles

    def reload_vehicles(self):
        """Fetches all vehicle records from the database and updates the internal list."""
        query = "SELECT * FROM vehicles"
        results = self._fetch_results(query)

        # Create vehicle objects using data from the dictionary
        self.vehicles = [self._create_vehicle_from_row(row) for row in results]

    def _create_vehicle_from_row(self, row):
        """Converts a database row into a Vehicle object."""
        return Vehicle(
            id=row['id'],
            model_year=row['year'],
            make=row['make'],
            model=row['model'],
            vehicle_class=row['v_class'],
            engine_size=row['engine_size'],
            cylinders=row['cylinders'],
            transmission=row['transmission'],
            fuel_type=row['fuel_type'],
            city_consumption=row['city_mpg'],
            highway_consumption=row['highway_mpg'],
            combined_consumption=row['combined_mpg'],
            co2_emissions=row['co2_emissions'],
            co2_rating=row['co2_rating'],
            smog_rating=row['smog_rating']
        )

    def add_vehicle(self, vehicle):
        """
        Adds a new vehicle to the database if it doesn't already exist.
        """
        # Check if the vehicle already exists
        check_query = """
        SELECT COUNT(*) FROM vehicles WHERE make = %s AND model = %s AND year = %s
        """
        check_params = (vehicle.make, vehicle.model, vehicle.model_year)
        existing_vehicle_count = self._fetch_results(check_query, check_params)

        if existing_vehicle_count and existing_vehicle_count[0]['COUNT(*)'] > 0:
            print(f"Vehicle {vehicle.make} {vehicle.model} {vehicle.model_year} already exists.")
            return  

        # Insert the new vehicle into the database
        query = """
        INSERT INTO vehicles (year, make, model, v_class, engine_size, cylinders,
                              transmission, fuel_type, city_mpg, highway_mpg, 
                              combined_mpg, co2_emissions, co2_rating, smog_rating)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            int(vehicle.model_year),  
            vehicle.make,
            vehicle.model,
            vehicle.vehicle_class,
            float(vehicle.engine_size), 
            int(vehicle.cylinders), 
            vehicle.transmission,  
            vehicle.fuel_type,
            float(vehicle.city_consumption),  # Ensure city_consumption is a float
            float(vehicle.highway_consumption),  # Ensure highway_consumption is a float
            float(vehicle.combined_consumption),  # Ensure combined_consumption is a float
            int(vehicle.co2_emissions),  # Ensure co2_emissions is an integer
            int(vehicle.co2_rating),  # Ensure co2_rating is an integer (was previously a string)
            int(vehicle.smog_rating)  # Ensure smog_rating is an integer
        )

        try:
            self._execute_query(query, params)  # Execute the query
            self.reload_vehicles()  # Refresh the vehicles list after adding a new vehicle
        except Exception as e:
            print(f"Error adding vehicle: {e}")

    def edit_vehicle(self, vehicle_id, vehicle):
        """
        Updates an existing vehicle record in the database.
        """
        # First, fetch the vehicle by its ID
        query = "SELECT * FROM vehicles WHERE id = %s"
        result = self._fetch_results(query, (vehicle_id,))
        if not result:
            raise ValueError(f"Vehicle with ID {vehicle_id} not found.")
        
        # Now, update the vehicle data
        update_query = """
        UPDATE vehicles
        SET year = %s, make = %s, model = %s, v_class = %s, engine_size = %s, cylinders = %s,
            transmission = %s, fuel_type = %s, city_mpg = %s, highway_mpg = %s,
            combined_mpg = %s, co2_emissions = %s, co2_rating = %s, smog_rating = %s
        WHERE id = %s
        """
        update_params = (
            vehicle.model_year, vehicle.make, vehicle.model, vehicle.vehicle_class, vehicle.engine_size,
            vehicle.cylinders, vehicle.transmission, vehicle.fuel_type, vehicle.city_consumption,
            vehicle.highway_consumption, vehicle.combined_consumption, vehicle.co2_emissions,
            vehicle.co2_rating, vehicle.smog_rating, vehicle_id
        )
        
        try:
            self._execute_query(update_query, update_params)
            self.reload_vehicles()  # Refresh the vehicles list after editing a vehicle
        except Exception as e:
            print(f"Error updating vehicle: {e}")
            raise

    def delete_vehicle(self, vehicle_id):
        """Deletes a vehicle record from the database by ID."""
        query = "DELETE FROM vehicles WHERE id = %s"
        self._execute_query(query, (vehicle_id,))
        self.reload_vehicles()  # Refresh the vehicles list after deletion

    def close(self):
        """Closes the database connection."""
        self.db.close_connection()

    def get_vehicle_by_id(self, vehicle_id):
        """
        Fetches a vehicle by its ID from the database.
        """
        query = "SELECT * FROM vehicles WHERE id = %s"
        result = self._fetch_results(query, (vehicle_id,))
        
        if result:
            # Return a Vehicle object
            return self._create_vehicle_from_row(result[0])
        return None  # Return None if not found
