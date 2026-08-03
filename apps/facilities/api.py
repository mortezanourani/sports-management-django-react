from ninja import Router
from ninja.errors import HttpError
from ninja.pagination import paginate
from ninja_jwt.authentication import JWTAuth
from django.shortcuts import get_object_or_404
from apps.accounts.permissions import require_role
from .schemas import *

router = Router(auth=JWTAuth())

@router.get('/', response=list[FacilityOut])
@paginate
def list_facilities(request, facility_type: str = None):
    queryset = Facility.objects.all()
    if facility_type:
        queryset = queryset.filter(facility_type=facility_type)
    return queryset

@router.get('/{facility_id}', response=FacilityOut)
def get_facility(request, facility_id: int):
    return get_object_or_404(Facility, pk=facility_id)

@router.post('/', response=FacilityOut)
@require_role('admin', 'manager', 'm88_officer', 'm5_officer')
def create_facility(request, payload: FacilityIn):
    if request.auth.role == 'm88_officer' and payload.facility_type != 'msy':
        raise HttpError(403, 'شما تنها مجاز به ثبت اماکن وزارت ورزش و جوانان هستید.')
    if request.auth.role == 'm5_officer' and payload.facility_type not in ('private', 'governmental'):
        raise HttpError(403, 'شما تنها مجاز به ثبت اماکن خصوصی و سایر ارگان ها هستید.')
    facility = Facility.objects.create(**payload.dict())
    return facility

@router.put('/{facility_id}', response=FacilityOut)
@require_role('admin', 'manager', 'm88_officer', 'm5_officer')
def update_facility(request, facility_id: int, payload: FacilityIn):
    facility = get_object_or_404(Facility, pk=facility_id)
    for attr, value in payload.dict().items():
        setattr(facility, attr, value)
    facility.save()
    return facility

@router.delete('/{facility_id}')
@require_role('admin', 'manager')
def delete_facility(request, facility_id: int):
    facility = get_object_or_404(Facility, pk=facility_id)
    facility.delete()
    return {'success': True}

# --- Nested: Contracts -----
@router.post('/contracts', response=dict)
@require_role('admin', 'manager', 'm88_officer')
def create_contract(request, payload: FacilityContractIn):
    facility = get_object_or_404(Facility, id=payload.facility)
    if facility.facility_type != 'msy':
        raise HttpError(400, 'فراردادها فقط برای اماکن وزارت ورزش و جوانان مجاز است.')
    contract = FacilityContract.objects.create(**payload.dict())
    return {'id': contract.id}

# --- Nested: Licenses -----
@router.post('/licenses', response=dict)
@require_role('admin', 'manager', 'm88_officer', 'm5_officer')
def create_license(request, payload: FacilityContractIn):
    license = FacilityLicense.objects.create(**payload.dict())
    return {'id': license.id}
