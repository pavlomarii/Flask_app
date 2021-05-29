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
    return 'Hello World'


if __name__ == '__main__':
    app.run()
