from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/Tomastemarc_Cell_DB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Agregar el from models import

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/producto")
def prendas():
    return render_template('producto.html')

@app.route("/agregar_producto")
def prendas():
    return render_template('agregar_producto.html')