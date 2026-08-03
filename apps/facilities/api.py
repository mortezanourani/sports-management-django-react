from ninja import Router
from ninja_jwt.authentication import JWTAuth
from apps.accounts.permissions import require_role
from .models import Facility

router = Router(auth=JWTAuth())

@router.get('/ping')
def ping(request):
    return {'status': 'ok'}

@router.post('/msy')
@require_role('admin', 'manager', 'm88_officer')
def create_msy_facility(request, payload: FacilitySchema):
    return {'status': 'ok'}