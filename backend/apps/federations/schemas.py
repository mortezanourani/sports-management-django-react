from ninja import ModelSchema
from .models import Federation, FederationPosition

class FederationIn(ModelSchema):
    class Meta:
        model = Federation
        fields = '__all__'

class FederationOut(ModelSchema):
    class Meta:
        model = Federation
        fields = '__all__'

class FederationPositionIn(ModelSchema):
    class Meta:
        model = FederationPosition
        fields = '__all__'

class FederationPositionOut(ModelSchema):
    class Meta:
        model = FederationPosition
        fields = '__all__'
