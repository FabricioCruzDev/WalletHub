from typing import Optional
import datetime
import uuid

from sqlalchemy import BigInteger, Boolean, Column, DateTime, Double, Numeric, PrimaryKeyConstraint, Table, Text, Uuid, text, func
from sqlalchemy.dialects.postgresql import OID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'tb_user'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='tb_user_pkey'),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid, 
        primary_key=True,
        default=uuid.uuid4, #cado o banco local não saiba gerar
        server_default=text('gen_random_uuid()')
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
        nullable=False
        )
    create_at: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        server_default=text('now()')
        )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        server_default=text('now()')
        )
    synced: Mapped[bool] = mapped_column(
        Boolean,
        server_default=text('false')
        )
    is_deleted: Mapped[bool] = mapped_column(
        Boolean,
        server_default=text('false'))
