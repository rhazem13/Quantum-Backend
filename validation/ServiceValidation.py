from marshmallow.validate import Length,Regexp
from marshmallow import Schema, fields


class CreateServiceScheme(Schema):
    class Meta:
        fields = ("name","description","type")
    name = fields.Str(required=True, validate=Length(max=80)) 
    description = fields.Str(required=True)
    type = fields.Bool(required=True)

class GetServiceScheme(Schema):
    class Meta:
        fields = ("id","name","photopath","description","type")
    id = fields.Int(required=True)
    name = fields.Str(required=True, validate=Length(max=80))
    photopath = fields.Str(required=True, validate=Length(max=255))
    description = fields.Str(required=True)
    type = fields.Bool(required=True)