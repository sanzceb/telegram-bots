#!/usr/bin/env python3

import csv
import pkgutil
import io
from functools import reduce


def read_data(fname):
    rawdata = pkgutil.get_data(__package__, f'data/{fname}')
    if not rawdata:
        raise SystemExit(f"{fname} not found")
    else:
        txtdata = io.StringIO(rawdata.decode('utf-8'))
        return [row for row in csv.DictReader(txtdata)]

_rows = read_data('club.csv')
clubs_by_name, clubs = {}, {}
for row in _rows:
    clubs_by_name[row['name_en']] = row
    clubs[row['ID']] = row

_rows = read_data('stadium.csv')
stadiums = {row['ID'] : row for row in _rows}

_rows = read_data('matchday.csv')
matchdays = {row['ID'] : row for row in _rows}

fixtures = read_data('fixture.csv')

def fix_repr(fix):
    mday = matchdays[fix['matchday']]
    date = mday['date']
    number = mday['number']
    home = clubs[fix['home']]
    away = clubs[fix['away']]
    stadium = stadiums[fix['stadium']]
    return f'{home['name_en']} - {away['name_en']}'\
         + f' | {stadium['name']}'\
         + f' | {date}'

def upcoming_fixtures(clubname):
    if clubname not in clubs_by_name:
        print(f'{clubname} not found')
        return None
    clubid = clubs_by_name[clubname]['ID']
    pred = lambda x: x['home'] == clubid\
            or x['away'] == clubid
    op = lambda x,y : f'{x}\n{y}'
    return reduce(op, map(fix_repr, filter(pred, fixtures)), '')

