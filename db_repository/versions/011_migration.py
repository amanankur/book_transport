from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
driver = Table('driver', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('first_name', VARCHAR(length=64)),
    Column('last_name', VARCHAR(length=64)),
    Column('contact', VARCHAR(length=120)),
    Column('vehicleNum', VARCHAR(length=120)),
    Column('booking_id', INTEGER),
)

booking = Table('booking', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('phoneNum', String(length=120)),
    Column('startLoc', String(length=120)),
    Column('endLoc', String(length=120)),
    Column('driver_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['driver'].columns['booking_id'].drop()
    post_meta.tables['booking'].columns['driver_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['driver'].columns['booking_id'].create()
    post_meta.tables['booking'].columns['driver_id'].drop()
