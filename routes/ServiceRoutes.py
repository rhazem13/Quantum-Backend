from validation.ServiceValidation import CreateServiceScheme, GetServiceScheme
from flask import Blueprint, request
from repositories.ServiceRepository import ServiceRepository

serviceRepository=ServiceRepository()
createServicecasescheme = CreateServiceScheme() 
service_bp = Blueprint('service',__name__)
servicescheme= GetServiceScheme(many=True)

@service_bp.post('')
def postservice():
    result = request.form
    errors = createServicecasescheme.validate(result)
    if errors:
        if(type(errors)==str):
            return {"error":errors}
        key = next(iter(errors))
        return {"error":key+' '+errors[key][0]} 
    try:
        photo = request.files['photo']
    except:
        return {"error":"Service Photo is required"}
    if(photo.filename== ''):
        return {"error":"Service Photo is required"}
    # try:
    serviceRepository.create(result, photo)
    return {"success":"created service successfully"}
    # except:
        # return {"error":"unknown error "}

@service_bp.get('')
def getServices():
    services = serviceRepository.get_all()
    return {
        "services": servicescheme.dump(services)
    }

@service_bp.delete('remove_service/<int:id>')
def remove_service(id):
    try :
        serviceRepository.remove_service(id)
        return {"success":"removed case"}
    except:
        return {"error":"unknown error"}