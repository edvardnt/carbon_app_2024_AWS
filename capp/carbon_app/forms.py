from flask_wtf import FlaskForm
from wtforms import  SubmitField,  SelectField,  FloatField
from wtforms.validators import InputRequired

class BusForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Diesel', 'Diesel'), ('Electric', 'Electric'), ('Biodiesel', 'Biodiesel')])
  submit = SubmitField('Submit')

class CarForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Old Petrol', 'Old Petrol Car'), ('Old Diesel', 'Old Diesel Car'),('New Diesel', 'New Diesel Car'), ('New Petrol', 'New Petrol Car'), ('Small Electric', 'Small Electric Car'), ('Medium Electric', 'Medium Electric Car'), ('Large Electric', 'Large Electric Car')])
  submit = SubmitField('Submit')  

class PlaneForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
   choices=[('Long-haul Economy class', 'Long-haul Economy class Plane'), ('Long-haul Business class', 'Long-haul Business Class Plane'), ('Long-haul First class', 'Long-haul First class Plane'), ('Short-haul Economy class', 'Short-haul Economy class Plane'), ('Short-haul Business class', 'Short-haul Business Class Plane'), ('Short-haul First class', 'Short-haul First class Plane')])
  submit = SubmitField('Submit')
  
class FerryForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Diesel', 'Diesel'), ('Electric', 'Electric'),])
  submit = SubmitField('Submit')  

class MotorbikeForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Petrol', 'Petrol')])
  submit = SubmitField('Submit')

class TrainForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
   choices=[('Diesel', 'Diesel'), ('Electric Nordic', 'Electric Nordic Train'), ('Electric European', 'Electric European Train')])

  submit = SubmitField('Submit')

class BicycleForm(FlaskForm):
    kms = FloatField('Kilometers', [InputRequired()])
    fuel_type = SelectField('Type of Fuel', [InputRequired()], 
                            choices=[('No fossil fuel', 'No fossil fuel')])
    submit = SubmitField('Submit')  

class WalkForm(FlaskForm):
    kms = FloatField('Kilometers', [InputRequired()])
    fuel_type = SelectField('Type of Fuel', [InputRequired()], 
                            choices=[('No fossil fuel', 'No fossil fuel')])
    submit = SubmitField('Submit')

