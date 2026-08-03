from django.db import models

class Facility(models.Model):
    class FacilityType(models.TextChoices):
        MSY = 'msy', 'دولتی ورزش و جوانان'
        PRIVATE = 'private', 'خصوصی (ماده 5)'
        GOV = 'governmental', 'دولتی سایر ارگان ها'

    class GeoType(models.TextChoices):
        Rural = 'rural', 'روستایی'
        Urban = 'urban', 'شهری'

    facility_type = models.CharField(max_length=30, choices=FacilityType.choices, default=FacilityType.MSY)
    name = models.CharField(max_length=255)
    geo_type = models.CharField(max_length=30, choices=GeoType.choices, default=GeoType.Urban)
    district = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=10)
    address = models.TextField()
    phone = models.CharField(max_length=11)
    area = models.FloatField(null=True, blank=True)
    hall_area = models.FloatField(null=True, blank=True)
    land_area = models.FloatField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    sport_type = models.CharField(max_length=255, blank=True)

    owner_name = models.CharField(max_length=255, blank=True)
    owner_contact = models.CharField(max_length=100, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} ({self.facility_type})'

class FacilityContract(models.Model):
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, related_name='contracts')
    contract_serial = models.CharField(max_length=30, null=True, blank=True)
    contractor_name = models.CharField(max_length=255)
    contractor_seen_code = models.CharField(max_length=10, null=True, blank=True)
    contractor_phone = models.CharField(max_length=11, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    contract_file = models.FileField(upload_to='facility_contracts/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f'Contract: {self.facility.name} ({self.contractor_name})'

class FacilityLicense(models.Model):
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, related_name='licenses')
    license_serial = models.CharField(max_length=30, null=True, blank=True)
    holder_name = models.CharField(max_length=255)
    is_renewal = models.BooleanField(default=False)
    issue_date = models.DateField()
    expiry_date = models.DateField(null=True, blank=True)
    license_file = models.FileField(upload_to='facility_licenses/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-issue_date']

    def __str__(self):
        return f'License {self.facility.name} ({self.license_serial})'