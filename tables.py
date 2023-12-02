from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DECIMAL
Base = declarative_base()

class Player(Base):
    __tablename__ = 'player'
    player_id = Column(Integer, primary_key=True, autoincrement=True)
    team_id = Column(Integer, nullable=False)
    uniform_num = Column(Integer, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    mpg = Column(Integer, nullable=False)
    ppg = Column(Integer, nullable=False)
    rpg = Column(Integer, nullable=False)
    apg = Column(Integer, nullable=False)
    spg = Column(DECIMAL(6, 1), nullable=False)
    bpg = Column(DECIMAL(6, 1), nullable=False)

class team(Base):
    __tablename__ = 'team'
    team_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    state_id = Column(Integer, nullable=False)
    color_id = Column(Integer, nullable=False)
    wins = Column(Integer, nullable=False)
    losses = Column(Integer, nullable=False)


class color(Base):
    __tablename__ = 'color'

    color_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

class state(Base):
    __tablename__ = 'state'
    state_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

