use vehicles;
CREATE DATABASE IF NOT EXISTS vehicles;
select * from vehicles;
CREATE TABLE vehicles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    year INT,
    make VARCHAR(255),
    model VARCHAR(255),
    v_class VARCHAR(255),
    engine_size FLOAT,
    cylinders INT,
    transmission VARCHAR(255),
    fuel_type VARCHAR(255),
    city_mpg FLOAT,
    highway_mpg FLOAT,
    combined_mpg FLOAT,
    co2_emissions INT,
    co2_rating VARCHAR(255),
    smog_rating VARCHAR(255)
);
-- drop table vehicles;

