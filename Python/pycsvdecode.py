#!/usr/bin/env python3
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import *
import csv

engine = create_engine('sqlite:////home/data.db')
Base = declarative_base()


class post_office(Base):
    __tablename__ = 'post_office'
    id = Column(Integer, primary_key=True)
    Officename = Column(String(20))
    Pincode = Column(String(6))
    Officetype = Column(String(5))
    Dstats = Column(String(15))
    Divname = Column(String(50))
    Regname = Column(String(50))
    Circlename = Column(String(50))
    Taluk = Column(String(50))
    Distname = Column(String(50))
    Statename = Column(String(50))
    Phnum = Column(String(50))
    RHO = Column(String(50))
    RSO = Column(String(50))


r = {
    'Officename': " ",
    'Pincode': " ",
    'Officetype': " ",
    'Dstats': " ",
    'Divname': " ",
    'Regname': " ",
    'Circlename': " ",
    'Taluk': " ",
    'Distname': " ",
    'Statename': " ",
    'Phnum': " ",
    'RHO': " ",
    'RSO': " "

}
Session = sessionmaker(bind=engine)
session = Session()
post_office.__table__.create(bind=engine, checkfirst=True)
with open('data.csv') as f:
    lines = csv.DictReader(f)
    for line in lines:
        r['Officename'] = line['officename'].upper()
        r['Pincode'] = line['pincode'].upper()
        r['Officetype'] = line['officeType'].upper()
        r['Dstats'] = line['Deliverystatus'].upper()
        r['Divname'] = line['divisionname'].upper()
        r['Regname'] = line['regionname'].upper()
        r['Circlename'] = line['circlename'].upper()
        r['Taluk'] = line['Taluk'].upper()
        r['Distname'] = line['Districtname'].upper()
        r['Statename'] = line['statename'].upper()
        r['Phnum'] = line['Telephone'].upper()
        r['RHO'] = line['Related Suboffice'].upper()
        r['RSO'] = line['Related Headoffice'].upper()
        row = post_office(**r)
        session.add(row)

session.commit()
