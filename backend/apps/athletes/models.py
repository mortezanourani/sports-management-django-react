from django.db import models

class Athletes(models.Model):
    federation = models.ForeignKey('federations.Federation', on_delete=models.CASCADE, related_name='athletes')
    year = models.PositiveIntegerField()
    month = models.PositiveIntegerField()
    men_count = models.PositiveIntegerField
    women_count = models.PositiveIntegerField

    class Meta:
        ordering = ['-year', '-month', 'federation']
