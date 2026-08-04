from ninja import Router
from .models import Athletes

public_router = Router()

@public_router.get('/stats/athletes')
def athlete_stats(request, federation_id: int = None, year: int = None):
    queryset = Athletes.objects.all()
    if federation_id: queryset = queryset.filter(federation_id=federation_id)
    if year: queryset = queryset.filter(year=year)
    return list(queryset.values('federation__name', 'year', 'month', 'gender', 'count'))