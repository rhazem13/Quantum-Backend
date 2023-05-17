# from validation.NeedycaseValidation import CreateNeedycasescheme, GetNeedycasescheme
# from flask import Blueprint, request, jsonify, Response, make_response
# from marshmallow import ValidationError
# from repositories.NeedycaseRepository import NeedycaseRepository
# from sqlalchemy.exc import IntegrityError
# from modelss.db import db
# import jwt
# from PIL import Image
# import io
# import sys
# import os
# import torch
# import cv2
# import numpy as np

# needycaseRepository=NeedycaseRepository()
# createNeedycasescheme = CreateNeedycasescheme() 
# needycase_bp = Blueprint('needycase',__name__)
# needycasescheme= GetNeedycasescheme(many=True)

# @needycase_bp.post('/register')
# def postneedycase():
#     result = request.form
#     errors = createNeedycasescheme.validate(result)
#     if errors:
#         if(type(errors)==str):
#             return {"error":errors}
#         key = next(iter(errors))
#         return {"error":key+' '+errors[key][0]} 
#     try:
#         case_paper = request.files['case_paper']
#     except:
#         return {"error":"برجاء ادخال صورة لاوراق الحالة"}
#     try:
#         case_photo = request.files['case_photo']
#     except:
#         return {"error":"برجاء ادخال صورة الحالة"}
#     if(case_paper.filename== ''):
#         return {"error":"برجاء ادخال صورة لاوراق الحالة"}
#     if(case_photo.filename== ''):
#         return {"error":"برجاء ادخال صورة الحالة"}
#     try:
#         needycaseRepository.create(result, case_paper, case_photo)
#         return {"success":"created needycase successfully"}
#     except:
#         return {"error":"unknown error "}
#     return {"error":"unknown error "}
    

# @needycase_bp.get('/all')
# def getHome():
#     cases = NeedycaseRepository.get_all()
#     return {
#         "cases": needycasescheme.dump(cases)
#     }

# @needycase_bp.get('/critical')
# def getcritical():
#     cases = NeedycaseRepository.get_cirtical()
#     return {
#         "cases": needycasescheme.dump(cases)
#     }

# @needycase_bp.get('pending_cases')
# def get_pending_cases():
#     token = None
#     if 'x-access-token' in request.headers:
#             print("got access token")
#             token = request.headers['x-access-token']
#     if not token:
#         return jsonify({'error' : 'Token is missing!'}), 401
#     try: 
#         data = jwt.decode(token,'secret', algorithms=['HS256'])
#         type = data['type']
#         if(type!='superadmin'):
#             return jsonify({'error' : 'you are not supposed to be here!'}), 401
#     except:
#         return jsonify({'error' : 'you are not supposed to be here!'}), 401
#     cases = NeedycaseRepository.get_pending_cases()
#     return needycasescheme.dump(cases)

# @needycase_bp.post('confirm_case/<int:id>')
# def confirm_case(id):
#     token = None
#     if 'x-access-token' in request.headers:
#             print("got access token")
#             token = request.headers['x-access-token']
#     if not token:
#         return jsonify({'error' : 'Token is missing!'}), 401
#     try: 
#         data = jwt.decode(token,'secret', algorithms=['HS256'])
#         type = data['type']
#         if(type!='superadmin'):
#             return jsonify({'error' : 'you are not supposed to be here!'}), 401
#     except:
#         return jsonify({'error' : 'you are not supposed to be here!'}), 401
#     try :
#         NeedycaseRepository.confirm_case(id)
#         return {"success":"confirmed case"}
#     except:
#         return {"error":"unknown error"}
#     return {"error":"unknown error"}

# @needycase_bp.post('remove_case/<int:id>')
# def remove_case(id):
#     token = None
#     if 'x-access-token' in request.headers:
#             print("got access token")
#             token = request.headers['x-access-token']
#     if not token:
#         return jsonify({'error' : 'Token is missing!'}), 401
#     try: 
#         data = jwt.decode(token,'secret', algorithms=['HS256'])
#         type = data['type']
#         if(type!='superadmin'):
#             return jsonify({'error' : 'you are not supposed to be here!'}), 401
#     except:
#         return jsonify({'error' : 'you are not supposed to be here!'}), 401
#     try :
#         NeedycaseRepository.remove_case(id)
#         return {"success":"removed case"}
#     except:
#         return {"error":"unknown error"}
#     return {"error":"unknown error"}