# Author: Prabjot Singh
# This file contains a Flask framework for managing vehicle records, including features to add, edit, delete, 
# reload, and save vehicles. The application interacts with vehicle data through the VehicleManager class and displays 
# information via HTML templates.

from flask import Flask, render_template, request, redirect, url_for, flash
from business.vehicle_manager import VehicleManager
from models.vehicle import Vehicle
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
vehicle_manager = VehicleManager('data/my2024-fuel-consumption-ratings.csv')

@app.route('/')
def index():
    """
    Renders the homepage displaying the list of all vehicles.
    """
    return render_template('index.html', vehicles=vehicle_manager.get_all_vehicles(), name="Prabjot Singh")

#  These are the routes for application follows html
@app.route('/add', methods=['GET', 'POST'])
def add_vehicle():
    """
    Handles the addition of a new vehicle record.
    """
    if request.method == 'POST':
        new_vehicle = Vehicle(
            model_year=request.form['model_year'],
            make=request.form['make'],
            model=request.form['model'],
            vehicle_class=request.form['vehicle_class'],
            engine_size=request.form['engine_size'],
            cylinders=request.form['cylinders'],
            transmission=request.form['transmission'],
            fuel_type=request.form['fuel_type'],
            city_consumption=request.form['city_consumption'],
            highway_consumption=request.form['highway_consumption'],
            combined_consumption=request.form['combined_consumption'],
            co2_emissions=request.form['co2_emissions']
        )
        vehicle_manager.add_vehicle(new_vehicle)
        flash('Vehicle added successfully!')
        return redirect(url_for('index'))
    return render_template('vehicle_form.html', action='Add')

#  These are the routes for application follows html
@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_vehicle(index):
    """
    Handles editing an existing vehicle record.
    Renders the vehicle_form.html template on GET, or redirects to the homepage on successful POST.
    """
    if request.method == 'POST':
        updated_vehicle = Vehicle(
            model_year=request.form['model_year'],
            make=request.form['make'],
            model=request.form['model'],
            vehicle_class=request.form['vehicle_class'],
            engine_size=request.form['engine_size'],
            cylinders=request.form['cylinders'],
            transmission=request.form['transmission'],
            fuel_type=request.form['fuel_type'],
            city_consumption=request.form['city_consumption'],
            highway_consumption=request.form['highway_consumption'],
            combined_consumption=request.form['combined_consumption'],
            co2_emissions=request.form['co2_emissions']
        )
        vehicle_manager.edit_vehicle(index, updated_vehicle)
        flash('Vehicle updated successfully!')
        return redirect(url_for('index'))
    vehicle = vehicle_manager.get_vehicle(index)
    return render_template('vehicle_form.html', vehicle=vehicle, action='Edit', index=index)
#  These are the routes for application follows html

@app.route('/delete/<int:index>')
def delete_vehicle(index):
    """
    Deletes a vehicle record from the list.
    """
    vehicle_manager.delete_vehicle(index)
    flash('Vehicle deleted successfully!')
    return redirect(url_for('index'))

@app.route('/reload')
def reload_data():
    """
    Reloads the vehicle data from the CSV file, replacing the in-memory data.
    """
    vehicle_manager.reload_data()
    flash('Data reloaded successfully!')
    return redirect(url_for('index'))
#  These are the routes for application follows html


@app.route('/save')
def save_data():
    """
    Saves the in-memory vehicle data to a new CSV file.
    """
    vehicle_manager.save_data('data/New.csv')
    flash('Data saved successfully!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
