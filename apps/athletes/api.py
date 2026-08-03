from ninja import Router
from ninja.errors import HttpError
from ninja.pagination import paginate
from ninja_jwt.authentication import JWTAuth
from django.shortcuts import get_object_or_404
from apps.accounts.permissions import require_role
from .schemas import *

router = Router(auth=JWTAuth())

@router.get('/', response=list[AthletesOut])
@paginate
def list_athletes(request):
    return Athletes.objects.all()

@router.get('/{athlete_id}', response=AthletesOut)
def get_athlete(request, athlete_id: int):
    return get_object_or_404(Athletes, pk=athlete_id)

@router.post('/', response=AthletesOut)
@require_role('admin', 'manager', 'insurance_officer')
def create_athlete(request, payload: AthletesIn):
    athletes = Athletes.objects.create(**payload.dict())
    return athletes

@router.put('/{athlete_id}', response=AthletesOut)
@require_role('admin', 'manager', 'sport_officer')
def update_athlete(request, athlete_id: int, payload: AthletesIn):
    athlete = Athletes.objects.get(Athletes, pk=athlete_id)
    for attr, value in payload.dict().items():
        setattr(athlete, attr, value)
    athlete.save()
    return athlete

@router.delete('/{athlete_id}')
@require_role('admin', 'manager', 'sport_officer')
def delete_athlete(request, athlete_id: int):
    athlete = Athletes.objects.get(Athletes, pk=athlete_id)
    athlete.delete()
    return {'success': True}
