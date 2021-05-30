import config
from flask_restful import Api
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config.Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)


@app.route('/')
def index():
    return {'message': 'Hello World'}, 200


from views import routes

