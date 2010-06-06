#coding=utf-8

import web
import uuid

db = web.database(dbn='sqlite', db='atcforge_sqlite.db')

def guid():
    return uuid.uuid4().hex
