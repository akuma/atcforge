#coding=utf-8

import web
import uuid

db = web.database(dbn='sqlite', db='atcforge.db')

def get_controls():
    return db.select('at_control', order='modify_time DESC')

def get_control(id):
    try:
        return db.select('at_control', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def new_control(name, encoding, is_enable, description):
    id = uuid.uuid4().hex
    db.insert('at_control', id=id, name=name, encoding=encoding, is_enable=is_enable, description=description)

def update_control(id, name, encoding, is_enable, description):
    db.update('at_control', where="id=$id", vars=locals(), name=name, encoding=encoding, is_enable=is_enable, description=description)

def del_control(id):
    db.delete('at_control', where="id=$id", vars=locals())
