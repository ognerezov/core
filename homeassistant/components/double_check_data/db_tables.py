from sqlalchemy import Column, Integer, ForeignKey, String, UniqueConstraint, Boolean, DateTime, Index
from sqlalchemy.orm import DeclarativeBase, Mapped, aliased, mapped_column, relationship
from sqlalchemy.types import TypeDecorator


class Base(DeclarativeBase):
    """Base class for tables."""


class ControlledDevice(Base):
    """Representation of statistics run."""

    __tablename__ = "controlled_devices"
    __table_args__ = ({})
    id = Column(Integer, primary_key=True)
    entity_id = Column(String, nullable= False, primary_key=True)
    power_consumption = Column(Integer, nullable, False)

    def __repr__(self) -> str:
        """Return string representation of instance for debugging."""
        return (
            f"<ControlledDevice(id={self.id},"
            f"<ControlledDevice(entity_id={self.entity_id},"
        )