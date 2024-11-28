import csv
from models.vehicle import Vehicle
from data.db import DB

class VehicleDBIO:
    """Initialising the values here"""
    def __init__(self, db_host, db_user, db_password, db_name="vehicles"):
        self.db_host = db_host
        self.db_user = db_user
        self.db_password = db_password
        self.db_name = db_name

    def convert_value(self, value, target_type):
        """Convert the value to the appropriate type. Typecasting happening here"""
        if value == "" or value is None:
            return None
        try:
            if target_type == int:
                return int(value)
            elif target_type == float:
                return float(value)
            elif target_type == str:
                return str(value)
            else:
                return value
        except ValueError:
            return None 

    def load_csv_to_db(self, csv_file_path):
        """Load vehicle data from a CSV file into the database."""
        with open(csv_file_path, newline='', encoding='ISO-8859-1') as csvfile:
            reader = csv.DictReader(csvfile)  
            with DB(self.db_host, self.db_user, self.db_password, self.db_name) as connection:
                for row in reader:
                    try:
                        vehicle = Vehicle(
                            model_year=self.convert_value(row['Model year'], int),
                            make=row['Make'],
                            model=row['Model'],
                            vehicle_class=row['Vehicle class'],
                            engine_size=self.convert_value(row['Engine size (L)'], float),
                            cylinders=self.convert_value(row['Cylinders'], int),
                            transmission=row['Transmission'],
                            fuel_type=row['Fuel type'],
                            city_consumption=self.convert_value(row['City (L/100 km)'], float),
                            highway_consumption=self.convert_value(row['Highway (L/100 km)'], float),
                            combined_consumption=self.convert_value(row['Combined (L/100 km)'], float),
                            co2_emissions=self.convert_value(row['CO2 emissions (g/km)'], int),
                            co2_rating=self.convert_value(row['CO2 rating'], int),
                            smog_rating=self.convert_value(row['Smog rating'], int)
                        )
                        connection.add_vehicle(vehicle)
                    except Exception as e:
                        print(f"Error inserting vehicle data: {e}")
                        continue
