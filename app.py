# author: prabjot Singh
# This class is entry point for webapp make server run.
# Please read the requisites in Documentation to make it work error free.
# This class has routes and conversion with some debugs.

from flask import Flask, render_template, request, redirect, url_for, flash
from business.vehicle_manager import VehicleManager
from persistence.vehicleFile import VehicleDBIO
from models.vehicle import Vehicle

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  

vehicle_manager = VehicleManager("localhost", "root", "prabjotpwd", "vehicles")
vehicle_dbio = VehicleDBIO("localhost", "root", "prabjotpwd", "vehicles")

@app.route('/search', methods=['GET', 'POST'])
def search_vehicles():
    if request.method == 'POST':
        make = request.form.get('make')
        model = request.form.get('model')
        year = request.form.get('year')
        fuel_type = request.form.get('fuel_type')

        vehicles = vehicle_manager.search_vehicles(make, model, year, fuel_type)
        return render_template('index.html', vehicles=vehicles)

    return render_template('search_form.html')


@app.route('/')
def index():
    vehicles = vehicle_manager.get_all_vehicles()
    return render_template('index.html', vehicles=vehicles)

@app.route('/add_vehicle', methods=['GET', 'POST'])
def add_vehicle():
    if request.method == 'POST':
        try:
            # Capture the form data and ensure proper conversion of numeric values
            vehicle = Vehicle(
                model_year=request.form['model_year'],
                make=request.form['make'],
                model=request.form['model'],
                vehicle_class=request.form['vehicle_class'],
                engine_size=float(request.form['engine_size']),  
                fuel_type=request.form['fuel_type'],
                city_consumption=float(request.form['city_consumption']),  
                highway_consumption=float(request.form['highway_consumption']),  
                combined_consumption=float(request.form['combined_consumption']),  
                co2_emissions=int(request.form['co2_emissions']),  
                cylinders=int(request.form['cylinders']),  
                transmission=request.form['transmission'],
                co2_rating=request.form['co2_rating'],
                smog_rating=request.form['smog_rating'] 
            )
            
            vehicle_manager.add_vehicle(vehicle)
            flash('Vehicle added successfully!', 'success')
        except Exception as e:
            flash(f'Error adding vehicle: {e}', 'danger')
        return redirect(url_for('index'))
    
    return render_template('add_vehicle.html', action="Add", vehicle=None)



@app.route('/reload_data')
def reload_data():
    vehicle_manager.reload_vehicles()  
    vehicles = vehicle_manager.get_all_vehicles()  
    flash('Data reloaded successfully! || Sometimes it wont reload please restart the app new tab', 'success')
    return render_template('index.html', vehicles=vehicles) 

@app.route('/import_csv', methods=['POST'])
def import_csv():
    try:
        csv_file_path = 'data/my2024-fuel-consumption-ratings.csv'
        vehicle_dbio.load_csv_to_db(csv_file_path)
        flash('CSV data imported successfully!', 'success')
    except Exception as e:
        flash(f'Error importing CSV: {e}', 'danger')
    
    return redirect(url_for('index'))

@app.route('/edit_vehicle/<int:vehicle_id>', methods=['GET', 'POST'])
def edit_vehicle(vehicle_id):
    vehicle = vehicle_manager.get_vehicle_by_id(vehicle_id)
    if not vehicle:
        flash('404! Vehicle dissapered', 'danger')
        return redirect(url_for('index'))
    if request.method == 'POST':
        try:
            # Update the vehicle object with new form data
            vehicle.model_year = int(request.form['model_year'])
            vehicle.make = request.form['make']
            vehicle.model = request.form['model']
            vehicle.vehicle_class = request.form['vehicle_class']
            vehicle.engine_size = float(request.form['engine_size'])
            vehicle.fuel_type = request.form['fuel_type']
            vehicle.city_consumption = float(request.form['city_consumption'])
            vehicle.highway_consumption = float(request.form['highway_consumption'])
            vehicle.combined_consumption = float(request.form['combined_consumption'])
            vehicle.co2_emissions = int(request.form['co2_emissions'])
            vehicle.cylinders = int(request.form['cylinders'])
            vehicle.transmission = request.form['transmission']
            vehicle.co2_rating = int(request.form['co2_rating'])
            vehicle.smog_rating = int(request.form['smog_rating'])

            vehicle_manager.edit_vehicle(vehicle_id, vehicle)
            flash('You did great job its Updated', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error: {e}', 'danger')

    return render_template('vehicle_form.html', vehicle=vehicle)


@app.route('/delete_vehicle/<int:vehicle_id>', methods=['GET'])
def delete_vehicle(vehicle_id):
    try:
        vehicle_manager.delete_vehicle(vehicle_id)
        flash('Vehicle is deleted now 😒', 'success')
    except Exception as e:
        flash(f'Its an error yo! {e}', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)