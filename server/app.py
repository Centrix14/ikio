from flask import Flask
from flask_cors import CORS

from blueprints.organization import organization_bp
from blueprints.tko import tko_bp
from blueprints.user import user_bp
"""Регистрация приложения и модулей"""
app = Flask(__name__)
CORS(app)

app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(organization_bp, url_prefix='/organization')
app.register_blueprint(tko_bp, url_prefix='/tko')


if __name__ == '__main__':
    app.run(port=10000)
