from validation.ServiceValidation import CreateServiceScheme, GetServiceScheme
from flask import Blueprint, request
from repositories.ServiceRepository import ServiceRepository

serviceRepository=ServiceRepository()
createServicecasescheme = CreateServiceScheme() 
service_bp = Blueprint('service',__name__)
servicescheme= GetServiceScheme(many=True)

@service_bp.post('')
def postservice():
    try:
        result = request.form
        errors = createServicecasescheme.validate(result)
        if errors:
            if isinstance(errors, str):
                return {"error": errors}
            key = next(iter(errors))
            return {"error": f"{key} {errors[key][0]}"}
        
        if 'photo' not in request.files:
            return {"error": "Service Photo is required"}
        
        photo = request.files['photo']
        if photo.filename == '':
            return {"error": "Service Photo is required"}
        
        serviceRepository.create(result, photo)
        return {"success": "Created service successfully"}
    
    except Exception as e:
        return {"error": str(e)}


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