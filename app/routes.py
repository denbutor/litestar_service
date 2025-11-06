from litestar import get, Litestar
from litestar.di import Provide
from litestar.exceptions import NotFoundException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.db import get_session
from app.models import OfferWall, OfferWallOffer
from app.schemas import OfferWallOut, OfferOut


async def _get_offerwall(session: AsyncSession, **filters) -> OfferWallOut:
    for key in filters.keys():
        if not hasattr(OfferWall, key):
            raise ValueError(f"Field '{key}' does not exist in OfferWall")

    stmt = (
        select(OfferWall)
        .filter_by(**filters)
        .options(joinedload(OfferWall.offers).joinedload(OfferWallOffer.offer))
    )

    res = await session.execute(stmt)
    wall: OfferWall | None = res.scalars().unique().one_or_none()

    if not wall:
        key, value = next(iter(filters.items()))
        raise NotFoundException(detail=f"OfferWall with {key}={value} not found")

    ordered = sorted(wall.offers, key=lambda o: o.order)
    offers = [o.offer for o in ordered]

    out = OfferWallOut.model_validate(wall)
    out.offers = [OfferOut.model_validate(o) for o in offers]
    return out


@get("/offerwalls/{token:str}")
async def get_offerwall_by_token(token: str, session: AsyncSession) -> OfferWallOut:
    return await _get_offerwall(session, token=token)


@get("/offerwalls/by_url/{url:str}")
async def get_offerwall_by_url(url: str, session: AsyncSession) -> OfferWallOut:
    return await _get_offerwall(session, url=url)


@get("/offerwalls/get_offer_names/")
async def get_offer_names() -> dict:
    return {"offer_names": ["credit", "loan", "insurance"]}


app = Litestar(
    route_handlers=[get_offerwall_by_token, get_offerwall_by_url, get_offer_names],
    dependencies={"session": Provide(get_session)},
)
