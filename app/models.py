import enum
import uuid
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Float,
    ForeignKey,
    Text,
    Enum,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()


class OfferNameEnum(str, enum.Enum):
    CREDIT = "credit"
    LOAN = "loan"
    INSURANCE = "insurance"


class Offer(Base):
    __tablename__ = "offers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    url = Column(String(1024), nullable=False)
    is_active = Column(Boolean, default=True)
    name = Column(Enum(OfferNameEnum), nullable=False)
    sum_to = Column(Integer, nullable=True)
    term_to = Column(Integer, nullable=True)
    percent_rate = Column(Float, nullable=True)

    walls = relationship("OfferWallOffer", back_populates="offer")


class OfferWall(Base):
    __tablename__ = "offer_walls"

    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(UUID(as_uuid=True), unique=True, default=uuid.uuid4, nullable=False)
    name = Column(String(256), nullable=False)
    url = Column(String(1024), nullable=True)
    description = Column(Text, nullable=True)

    offers = relationship("OfferWallOffer", back_populates="wall", order_by="OfferWallOffer.order")


class OfferWallOffer(Base):
    __tablename__ = "offer_wall_offers"
    __table_args__ = (UniqueConstraint("wall_id", "offer_id", name="uq_wall_offer"),)

    id = Column(Integer, primary_key=True, autoincrement=True)
    wall_id = Column(Integer, ForeignKey("offer_walls.id", ondelete="CASCADE"), nullable=False)
    offer_id = Column(Integer, ForeignKey("offers.id", ondelete="CASCADE"), nullable=False)
    order = Column(Integer, nullable=False, default=0)

    wall = relationship("OfferWall", back_populates="offers")
    offer = relationship("Offer", back_populates="walls")