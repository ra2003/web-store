from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail

app = Flask(__name__)
app.debug = True
app.secret_key = 'kjsdhfssdkf'
app.csrf_enabled = True
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://cristi:1234@localhost/"\
										"test_web_store_db"
# Setting needed for mail server.
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'magazin.licenta@gmail.com'
app.config['MAIL_PASSWORD'] = 'licenta123'
app.config['ADMINS'] = ['magazin.licenta@gmail.com']

# Create the mai object
mail = Mail(app)

db = SQLAlchemy(app)


