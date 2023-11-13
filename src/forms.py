from flask_wtf import FlaskForm 
from flask_wtf import FlaskForm
from wtforms import StringField, FileField
from wtforms.validators import DataRequired, Optional

class InscriptionForm(FlaskForm):
    class Meta:
        csrf = False
    
    nom = StringField("Nom", validators=[DataRequired()])
    prenom = StringField("Prenom", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    phone_number = StringField("Phone Number", validators=[DataRequired()])
    address = StringField("Addresse", validators=[DataRequired()])

class ConnexionForm(FlaskForm):
    class Meta:
        csrf = False
    
    email = StringField("Email", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
