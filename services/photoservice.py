import cloudinary
import cloudinary.uploader

class PhotoService:
    photoService = None
    cloudinary.config(cloud_name = 'dnjijt3gv', api_key='722988112696177', 
    api_secret='RNP1NIAsoBvmZVlA8D62aIQmE0w')
    @staticmethod
    def getInstance():
        if not PhotoService.photoService:
            PhotoService.photoService = PhotoService()
        return PhotoService.photoService
    
    def addPhoto(self, photo,destFolder):
        upload_result = cloudinary.uploader.upload(photo,folder=destFolder)
        return upload_result['secure_url']