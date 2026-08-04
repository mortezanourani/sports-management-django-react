from ninja import ModelSchema
from .models import Champion, Medals

class ChampionIn(ModelSchema):
    class Meta:
        model = Champion
        fields = [
            'first_name',
            'last_name',
            'seen_code',
            'gender',
            'phone',
            'federation',
            'photo'
        ]

class ChampionOut(ModelSchema):
    class Meta:
        model = Champion
        fields = '__all__'

class MedalsIn(ModelSchema):
    class Meta:
        model = Medals
        fields = [
            'champion',
            'medal_type',
            'competition_name',
            'year'
        ]

class MedalsOut(ModelSchema):
    class Meta:
        model = Medals
        fields = '__all__'
