from ninja import ModelSchema, Schema
from .models import Facility, FacilityContract, FacilityLicense

class FacilityIn(ModelSchema):
    class Meta:
        model = Facility
        fields = [
            'facility_type',
            'name', 'geo_type',
            'district',
            'zip_code',
            'address',
            'phone',
            'area',
            'hall_area',
            'land_area',
            'is_active',
            'sport_type',
            'owner_name',
            'owner_contact'
        ]

class FacilityOut(ModelSchema):
    class Meta:
        model = Facility
        fields = '__all__'

class FacilityContractIn(ModelSchema):
    class Meta:
        model = FacilityContract
        fields = [
            'facility',
            'contract_serial',
            'contractor_name',
            'contractor_seen_code',
            'contractor_phone',
            'start_date',
            'end_date',
            'contract_file'
        ]

class FacilityLicenseIn(ModelSchema):
    class Meta:
        model = FacilityLicense
        fields = [
            'facility',
            'license_serial',
            'holder_name',
            'is_renewal',
            'issue_date',
            'expiry_date',
            'license_file'
        ]