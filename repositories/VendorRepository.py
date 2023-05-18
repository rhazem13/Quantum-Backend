from models.db import db
from models.vendor.VendorModel import Vendor
from services.photoservice import PhotoService

photoService=PhotoService.getInstance()

class VendorRepository:
    def get_all(self):
        return Vendor.query.all()
    
    def create(self, result, photo):
        photopath = photoService.addPhoto(photo, 'vendors')
        new_value = Vendor(**result)
        new_value.photopath = photopath

        # Convert 'type' value to boolean
        new_value.type = result.get('type') == 'true'  # or result.get('type') == 'True'

        db.session.add(new_value)
        db.session.commit()
        db.session.refresh(new_value)
        return new_value
    
    def get_by_id(id):
        return Vendor.query.get(id)
    
    def remove_vendor(self,id):
        vendor = Vendor.query.get(id)
        db.session.delete(vendor)
        db.session.commit()