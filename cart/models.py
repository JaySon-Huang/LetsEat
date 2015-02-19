from django.db import models


class Cart(object):
    def __init__(self):
        self.items = {}
        self.size = 0

    def add(self,cuisineID):
        if cuisineID in self.items:
            self.items[cuisineID] += 1
        else:
            self.items[cuisineID] = 1
        self.size += 1
        return self.size

    def clear():
        self.items = {}
        self.size = 0
