from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
db = SQLAlchemy(app)

if __name__ == "__main__":

    from views import *

    app.run(debug=True)
