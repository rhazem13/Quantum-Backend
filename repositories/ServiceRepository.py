from models.db import db
from models.service.ServiceModel import Service
from services.photoservice import PhotoService

photoService=PhotoService.getInstance()

class ServiceRepository:
    def get_all(self):
        return Service.query.all()

    def create(self, result, photo):
        photopath = photoService.addPhoto(photo, 'services')
        new_value = Service(**result)
        new_value.photopath = photopath

        # Convert 'type' value to boolean
        new_value.type = result.get('type') == 'true'  # or result.get('type') == 'True'

        db.session.add(new_value)
        db.session.commit()
        db.session.refresh(new_value)
        return new_value
    
    def get_by_id(id):
        return Service.query.get(id)
    
    def remove_service(self,id):
        service = Service.query.get(id)
        db.session.delete(service)
        db.session.commit()