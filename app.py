from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from routes.TestRoutes import test_bp
from routes.ServiceRoutes import service_bp
from routes.VendorRoutes import vendor_bp
from routes.auth import auth_bp
from models.db import db
from models.vendor.VendorModel import Vendor
from models.service.ServiceModel import Service
from sqlalchemy import text
# import jwt
from urllib.parse import quote

app = Flask(__name__)
CORS(app)
api = Api(app)
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,x-access-token,x-reset-token')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Hazm1102001@localhost:5432/Quantum'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://quantum_mg7q_user:5Z6T3K3TNbNrSi9UbgbllyU0O1hfxIA5@dpg-chj1kqe4dad01aii9t6g-a.frankfurt-postgres.render.com/quantum_mg7q'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:quantum@35.184.166.205/postgres'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.secret_key = 'secret string'
db.init_app(app)
with app.app_context():
    # query = text("ALTER TABLE services ALTER COLUMN description TYPE text")
    # db.engine.connect().execute(query)
    db.create_all()
app.register_blueprint(test_bp, url_prefix='/test')
app.register_blueprint(service_bp, url_prefix='/service')
app.register_blueprint(vendor_bp, url_prefix='/vendor')
app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == "__main__":
    app.run(debug=True)