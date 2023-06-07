from flask import Blueprint, request, jsonify
import jwt
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

from datetime import datetime, timedelta
auth_bp = Blueprint('auth',__name__)
SECRET_KEY = 'T&MY%8p3@Chdwd6u'

@auth_bp.post('login')
def login():
    # Retrieve the username and password from the request
    username = request.json.get('username')
    password = request.json.get('password')

    # Check if the provided credentials are valid
    if username == 'admin' and password == 'Yvy)5qpZfH&J%WGF':
        # Return a token as a response
        return jsonify({'token': generate_token(username)}), 200

    # If the credentials are invalid, return an error response
    return jsonify({'message': 'Invalid username or password'}), 401


def generate_token(username):
    # Set the token's payload with the username and expiration time
    payload = {
        'username': username,
        'exp': datetime.utcnow() + timedelta(hours=24)  # Token expiration time
    }

    # Generate the JWT token using the payload and secret key
    # token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    # Return the encoded token
    return "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjg2MjQxMTEzfQ.Dwoep3xhdzgSIWW7DlZw8MD-QeU-sdDri6PY6oEkv9M"