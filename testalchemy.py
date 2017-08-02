from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Persona(Base):
    __tablename__= 'persona'
    id=Column(Integer, primary_key=True)
    nombre=Column(String(250), nullable=False)

engine = create_engine('mysql+pymysql://root:root@localhost/soporteorm',echo=True)
Base.metadata.bind=engine

DBSession=sessionmaker()
DBSession.bind =engine
session=DBSession()

def crearTabla():
    Base.metadata.create_all(engine)
crearTabla()

p = Persona()
p.nombre = 'Dami'
#session.add(p)
session.commit()

lp = session.query(Persona).all()
for p in lp:
    print(p.nombre)
