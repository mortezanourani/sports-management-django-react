from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_extra import NinjaExtraAPI

api = NinjaExtraAPI(title='Sports Management API')
api.register_controllers(NinjaJWTDefaultController)

from apps.facilities.api import router as facilities_router
from apps.federations.api import router as federations_router
from apps.athletes.api import router as athletes_router
from apps.champions.api import router as champions_router
from apps.messaging.api import router as messaging_router

api.add_router('/athletes', athletes_router, tags=['Athletes'])
api.add_router('/champions', champions_router, tags=['Champions'])
api.add_router('/facilities', facilities_router, tags=['Facilities'])
api.add_router('/federations', federations_router, tags=['Federations'])
api.add_router('/messaging', messaging_router, tags=['Messaging'])

from apps.athletes.api_public import public_router as athletes_public_router

api.add_router('/public/athletes', athletes_public_router, tags=['Athletes'])
