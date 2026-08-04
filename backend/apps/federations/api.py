from ninja import Router
from ninja.errors import HttpError
from ninja.pagination import paginate
from ninja_jwt.authentication import JWTAuth
from django.shortcuts import get_object_or_404
from apps.accounts.permissions import require_role
from .schemas import *

router = Router(auth=JWTAuth())

@router.get('/', response=list[FederationOut])
@paginate
def list_federations(request):
    federations = Federation.objects.all()
    return federations

@router.get('/{federation_id}', response=FederationOut)
def get_federation(request, federation_id: int):
    return get_object_or_404(Federation, pk=federation_id)

@router.post('/', response=FederationOut)
@require_role('admin', 'manager')
def create_federation(request, payload: FederationIn):
    federation = Federation.objects.create(**payload.dict())
    return federation

@router.put('/{federation_id}', response=FederationOut)
@require_role('admin', 'manager')
def update_federation(request, federation_id: int, payload: FederationIn):
    federation = get_object_or_404(Federation, pk=federation_id)
    for attr, value in payload.dict().items():
        setattr(federation, attr, value)
    federation.save()
    return federation

@router.delete('/{federation_id}')
@require_role('admin', 'manager')
def delete_federation(request, federation_id: int):
    federation = get_object_or_404(Federation, pk=federation_id)
    federation.delete()
    return {'success': True}

# --- Nested: Position -----
@router.get('/{federation_id}/positions', response=list[FederationPositionOut])
def positions_history(request, federation_id: int):
    federation = get_object_or_404(Federation, pk=federation_id)
    positions = FederationPosition.objects.filter(federation=federation)
    return positions

@router.post('/positions', response=dict)
@require_role('admin', 'manager')
def create_federation_position(request, payload: FederationPositionIn):
    position = FederationPosition.objects.create(**payload.dict())
    return {'id': position.id}
