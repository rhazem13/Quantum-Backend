import cloudinary
import cloudinary.uploader

class PhotoService:
    photoService = None
    cloudinary.config(cloud_name = 'dvih3jm9h', api_key='171679492388358', 
    api_secret='kHKESxLIwAURv2ZZA-2r5gH8MeA')
    @staticmethod
    def getInstance():
        if not PhotoService.photoService:
            PhotoService.photoService = PhotoService()
        return PhotoService.photoService
    
    def addPhoto(self, photo,destFolder):
        upload_result = cloudinary.uploader.upload(photo,folder=destFolder)
        return upload_result['secure_url']