from django.db import models

class Federation(models.Model):
    name = models.CharField(max_length=255)
    is_para = models.BooleanField(default=False)
    is_championship = models.BooleanField(default=False)
    is_general = models.BooleanField(default=False)
    national_id = models.CharField(max_length=30, null=True, blank=True)
    district = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    is_active = models.BooleanField(default=True)

class FederationPosition(models.Model):
    class Position(models.TextChoices):
        PRESIDENT = 'president', 'رئیس هیات'
        MISS = 'miss', 'نائب رئیس هیات'
        VICE = 'vice', 'دبیر هیات'

    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='federation_positions')
    federation = models.ForeignKey('federations.Federation', on_delete=models.CASCADE, related_name='positions')
    position = models.CharField(choices=Position.choices, default=Position.PRESIDENT, max_length=20)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-start_date']