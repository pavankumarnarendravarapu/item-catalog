import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    name = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
            'email': self.email,
            'picture': self.picture
            }


class College(Base):
    __tablename__ = 'college'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return{
            'name': self.name,
            'id': self.id
            }


class Branch(Base):
    __tablename__ = 'branch'
    branch_name = Column(String(100), nullable=False)
    id = Column(Integer, primary_key=True)
    about = Column(String(250))
    class_strength = Column(String(100))
    labs = Column(Integer)
    faculties = Column(Integer)
    block = Column(String(100))
    branch_id = Column(Integer, ForeignKey('college.id'))
    college = relationship(College)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return{
            'branch_name': self.branch_name,
            'about': self.about,
            'id': self.id,
            'class_strength': self.class_strength,
            'labs': self.labs,
            'faculties': self.faculties,
            'block': self.block,
            'branch_id': self.branch_id
            }
engine = create_engine('sqlite:///collegedata.db')
Base.metadata.create_all(engine)
