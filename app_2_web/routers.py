from .models import *

class MyDBRouterNames(object):
    def db_for_read(self, model, **hints):
        if model == FirmName:
            return 'prices'
        return None

    def db_for_write(self, model, **hints):
        if model == FirmName:
            return 'prices'
        return None

class MyDBRouter(object):

    def db_for_read(self, model, **hints):
        if model == FirmInfo:
            return 'prices'
        return None

    def db_for_write(self, model, **hints):
        if model == FirmInfo:
            return 'prices'
        return None