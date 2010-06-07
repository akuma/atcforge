#coding=utf-8

import model
from model import db

### Function CRUD
def get_functions(action_id):
    return db.select('at_function', where='action_id=$action_id', order='modify_time DESC', vars=locals())

def get_function(id):
    try:
        return db.select('at_function', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def new_function(action_id, name, state, description):
    id = model.guid()
    db.insert('at_function', id=id, action_id=action_id, name=name, state=state, description=description)

def update_function(id, name, state, description):
    db.update('at_function', where="id=$id", vars=locals(), name=name, state=state, description=description)

def del_function(id):
    db.delete('at_function', where="id=$id", vars=locals())
