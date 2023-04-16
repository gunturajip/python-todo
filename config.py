from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://'+str(os.getenv('PGUSER'))+':'+str(os.getenv('PGPASSWORD'))+'@'+str(os.getenv('PGHOST'))+':'+str(os.getenv('PGPORT'))+'/'+str(os.getenv('PGDATABASE'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['WTF_CSRF_ENABLED'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)