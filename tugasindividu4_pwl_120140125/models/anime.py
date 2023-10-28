from sqlalchemy import Column, Integer, Text, DATETIME
from datetime import datetime

from .meta import Base


class Anime(Base):
    __tablename__ = "anime"
    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    studios = Column(Text, nullable=False)
    duration = Column(Text, nullable=False)
    created_at = Column(DATETIME, default=datetime.now)
