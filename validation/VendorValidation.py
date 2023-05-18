from marshmallow.validate import Length,Regexp
from marshmallow import Schema, fields


class CreateVendorScheme(Schema):
    class Meta:
        fields = ("name","description","photo","websiteurl")
    name = fields.Str(required=True, validate=Length(max=80)) 
    description = fields.Str(required=True)
    websiteurl = fields.Str(required=True, validate=Length(max=255)) 

class GetVendorScheme(Schema):
    class Meta:
        fields = ("id","name","photopath","description","websiteurl")
    id = fields.Int(required=True)
    name = fields.Str(required=True, validate=Length(max=80))
    photopath = fields.Str(required=True, validate=Length(max=255))
    description = fields.Str(required=True)
    websiteurl = fields.Str(required=True, validate=Length(max=255))