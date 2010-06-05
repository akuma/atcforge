#coding=utf-8

import web
#import uuid
import database.*

#db = web.database(dbn='sqlite', db='atcforge.db')

### Product CRUD
def get_products():
    return db.select('at_product', order='creation_time DESC')

def get_product(id):
    try:
        return db.select('at_product', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def new_product(ename, cname, description):
    db.insert('at_product', id=uuid(), ename=ename, cname=cname, description=description)

def update_product(id, cname, ename, description):
    db.update('at_product', where="id=$id", vars=locals(), cname=cname, ename=ename, description=description)

def del_product(id):
    db.delete('at_product', where="id=$id", vars=locals())
