from ninja import Router
from ninja.errors import HttpError
from ninja.pagination import paginate
from ninja_jwt.authentication import JWTAuth
from django.shortcuts import get_object_or_404
from apps.accounts.permissions import require_role
from .schemas import *

router = Router(auth=JWTAuth())

@router.get('/', response=list[ChampionOut])
@paginate
def list_champions(request):
    return Champion.objects.all()

@router.get('/{champion_id}', response=ChampionOut)
def get_champion(request, champion_id: int):
    return get_object_or_404(Champion, pk=champion_id)

@router.post('/', response=ChampionOut)
@require_role('admin', 'manager', 'sport_officer')
def create_champion(request, payload: ChampionIn):
    champion = Champion.objects.create(**payload.dict())
    return champion

@router.put('/{champion_id}', response=ChampionOut)
@require_role('admin', 'manager', 'sport_officer')
def update_champion(request, champion_id: int, payload: ChampionIn):
    champion = get_object_or_404(Champion, pk=champion_id)
    for attr, value in payload.dict().items():
        setattr(champion, attr, value)
    champion.save()
    return champion

@router.delete('/{champion_id}')
@require_role('admin', 'manager', 'sport_officer')
def delete_champion(request, champion_id: int):
    champion = get_object_or_404(Champion, pk=champion_id)
    champion.delete()
    return {'success': True}

# --- Nested: Medal -----
@router.post('/medals', response=dict)
@require_role('admin', 'manager', 'sport_officer')
def create_medals(request, payload: MedalsIn):
    medal = Medals.objects.create(**payload.dict())
    return {'id': medal.id}
