from ninja import NinjaAPI

api = NinjaAPI(title='Sports Management API')

from apps.facilities.api import router as facilities_router
from apps.federations.api import router as federations_router
from apps.athletes.api import router as athletes_router
from apps.champions.api import router as champions_router
from apps.messaging.api import router as messaging_router

api.add_router('/facilities', facilities_router)
api.add_router('/federations', federations_router)
api.add_router('/athletes', athletes_router)
api.add_router('/champions', champions_router)
api.add_router('/messaging', messaging_router)
