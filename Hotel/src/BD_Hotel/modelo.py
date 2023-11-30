from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine("sqlite:///hotel.db")

metadata = MetaData()

# Tabla `managers`
managers = Table(
    "managers",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column('phone_number', Integer),
    Column("location", String(50)),
)

# Tabla `inventory`

inventory = Table(
    "inventory",metadata,
    Column("id", Integer, primary_key=True),
    Column("type", String(50)),
    Column("status", String(50)),
    Column("location", String(50)),
)

# Tabla `guests`

guests = Table(
    "guests",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("phone_number", Integer),
    Column("address", String(50)),
    Column("room_number", Integer),
)