# Author: Prabjot Singh
# This file contains the VehicleManager class which handles CRUD operations for vehicle records in a MySQL database.


import mysql.connector
from mysql.connector import Error

class DB:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        """Establishes a database connection."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            self.cursor = None  

    def execute_query(self, query, params=None):
        """Executes a query on the database."""
        if not self.cursor:
            raise ConnectionError("Database connection failed. Or please create Database in your localhost first")
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.connection.commit()

    def fetch_results(self, query, params=None):
        """Fetches results from the database."""
        if not self.cursor:
            raise ConnectionError("Database connection failed. Please make db schema first")
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def add_vehicle(self, vehicle):
        """Inserts a vehicle into the database."""
        query = """
        INSERT INTO vehicles (year, make, model, v_class, engine_size, cylinders,
                              transmission, fuel_type, city_mpg, highway_mpg, 
                              combined_mpg, co2_emissions, co2_rating, smog_rating)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            vehicle.model_year, vehicle.make, vehicle.model, vehicle.vehicle_class, vehicle.engine_size,
            vehicle.cylinders, vehicle.transmission, vehicle.fuel_type, vehicle.city_consumption,
            vehicle.highway_consumption, vehicle.combined_consumption, vehicle.co2_emissions,
            vehicle.co2_rating, vehicle.smog_rating
        )
        self.execute_query(query, params)

    def close_connection(self):
        """Closes the database connection."""
        if self.connection and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()

    def __enter__(self):
        """Enter the runtime context related to this object."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit the runtime context related to this object."""
        self.close_connection()
