from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from routes.TestRoutes import test_bp
from models.db import db
from models.vendor.VendorModel import Vendor
from models.service.ServiceModel import Service

app = Flask(__name__)
CORS(app)
api = Api(app)
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,x-access-token,x-reset-token')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Hazm1102001@localhost:5432/Quantum'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.secret_key = 'secret string'
db.init_app(app)
with app.app_context():
    db.create_all()
app.register_blueprint(test_bp, url_prefix='/test')

if __name__ == "__main__":
    app.run(debug=True)