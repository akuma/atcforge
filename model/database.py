#coding=utf-8

import web
import uuid

db = web.database(dbn='sqlite', db='atcforge_sqlite.db')

def uuid():
    return uuid.uuid4().hex
