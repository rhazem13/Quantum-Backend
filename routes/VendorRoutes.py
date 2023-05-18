from validation.VendorValidation import CreateVendorScheme, GetVendorScheme
from flask import Blueprint, request
from repositories.VendorRepository import VendorRepository

vendorRepository=VendorRepository()
createvendorscheme = CreateVendorScheme() 
vendor_bp = Blueprint('vendor',__name__)
vendorscheme= GetVendorScheme(many=True)

@vendor_bp.post('')
def postvendor():
    result = request.form
    errors = createvendorscheme.validate(result)
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
    vendorRepository.create(result, photo)
    return {"success":"created service successfully"}
    # except:
        # return {"error":"unknown error "}

@vendor_bp.get('')
def getVendors():
    vendors = vendorRepository.get_all()
    return {
        "vendors": vendorscheme.dump(vendors)
    }

@vendor_bp.delete('remove_vendor/<int:id>')
def remove_vendor(id):
    try :
        vendorRepository.remove_vendor(id)
        return {"success":"removed vendor"}
    except:
        return {"error":"unknown error"}