#!/usr/bin/env python

import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import deferred, mapper, relationship, column_property, object_session, validates
from sqlalchemy import join, Table, MetaData, select, func, and_, Column, ForeignKey, Integer, String, Text, Binary

Base = declarative_base()
engine = create_engine('sqlite:///testdb', echo=True)


class Book(Base):
    __tablename__ = 'book'
    book_id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    summary = Column(String(2000))
    excerpt = deferred(Column(Text))
    photo1 = deferred(Column(Binary), group='photos')
    photo2 = deferred(Column(Binary), group='photos')
    photo3 = deferred(Column(Binary), group='photos')


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    addresses = relationship("Address")

    @validates('addresses')
    def validate_address(self, key, address):
        assert '@' in address.email
        return address

    @property
    def fullname(self):
        return self.firstname + ' ' + self.lastname

    @property
    def address_count(self):
        return object_session(self).\
            scalar(select([func.count(Address.id)]).
                   where(Address.user_id == self.id))


Base.metadata.create_all(engine)
ed1_user = User()
ed1_user.firstname = 'ed1'
ed1_user.lastname = 'Ed1 Jones'

from sqlalchemy.orm import Session
ses = Session(bind=engine)
ses.add(ed1_user)
ses.commit()
