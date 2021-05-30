import config
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config.Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import departments, employees


@app.route('/')
def index():
    return {'message': 'Hello World'}, 200


if __name__ == '__main__':
    app.run()
