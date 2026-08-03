from ninja import ModelSchema
from .models import Athletes

class AthletesIn(ModelSchema):
    class Meta:
        model = Athletes
        fields = '__all__'

class AthletesOut(ModelSchema):
    class Meta:
        model = Athletes
        fields = '__all__'
