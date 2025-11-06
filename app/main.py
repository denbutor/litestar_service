from litestar import Litestar

from app import models
from app.db import engine
from app.routes import *

app = Litestar(route_handlers=[get_offerwall_by_token, get_offerwall_by_url, get_offer_names])

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)