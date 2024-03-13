from mongoengine import *

connect('local')

class Property(Document):
    property_type = StringField(required=True)
    neighborhood = StringField(required=True)
    source_id = StringField(required=True)
    value = StringField(required=True)
    rooms = StringField(required=True)
    garage = StringField(required=True)
    m2 = StringField(required=True)
    title = StringField(required=True)
    description = StringField(required=True)
    real_state = StringField(required=True)
    property_features = StringField(required=True)
    condo_features = StringField(required=True)

p = Property(property_type='Apartamento', neighborhood='Centro').save()