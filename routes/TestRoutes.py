from flask import Blueprint, request, jsonify, Response, make_response

test_bp = Blueprint('test',__name__)


@test_bp.get('')
def gettest():
    return jsonify({'message':'test get'})
