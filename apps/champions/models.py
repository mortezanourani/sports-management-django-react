from django.db import models

class Champion(models.Model):
    class Gender(models.TextChoices):
        MALE = 'male', 'آقا'
        FEMALE = 'female', 'خانم'

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    seen_code = models.CharField(max_length=10, blank=True)
    gender = models.CharField(choices=Gender.choices, max_length=10)
    phone = models.CharField(max_length=11, blank=True)
    federation = models.ForeignKey('federations.Federation', on_delete=models.PROTECT, related_name='champions')
    photo = models.ImageField(upload_to='champions/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Medals(models.Model):
    class MedalsType(models.TextChoices):
        GOLD = 'gold', 'طلا'
        SILVER = 'silver', 'نقره'
        BRONZE = 'bronze', 'برنز'

    champion = models.ForeignKey(Champion, on_delete=models.CASCADE, related_name='medals')
    medal_type = models.CharField(choices=MedalsType.choices, max_length=10)
    competition_name = models.CharField(max_length=255)
    year = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-year']

    def __str__(self):
        return f'{self.champion.first_name} {self.champion.first_name} - {self.medal_type} ({self.year})'
