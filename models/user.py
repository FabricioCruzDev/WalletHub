from typing import Optional
import datetime
import uuid

from sqlalchemy import BigInteger, Boolean, Column, DateTime, Double, Numeric, PrimaryKeyConstraint, Table, Text, Uuid, text, func, false
from sqlalchemy.dialects.postgresql import OID
from sqlalchemy.orm import Mapped, mapped_column

from database.local_conn import Session, Base


class User(Base):

    def __init__(self, name, last_name, email):
        self.name = name
        self.last_name = last_name
        self.email = email
    
    __tablename__ = 'tb_user'


    id: Mapped[uuid.UUID] = mapped_column(
        Uuid, 
        primary_key=True,
        default=uuid.uuid4
        )
    name: Mapped[str] = mapped_column(
        Text,
        nullable=False
        )
    last_name: Mapped[str] = mapped_column(
        Text,
        nullable=False
        )
    email: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        unique=True
        )
    create_at: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        server_default=func.now()
        )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
        )
    synced: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        server_default=false()
        )
    is_deleted: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        server_default=false()
    )

