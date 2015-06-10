import json


class Cart(object):
    def __init__(self):
        self.items = {}
        self.size = 0

    def add(self, cuisineID):
        if cuisineID in self.items:
            self.items[cuisineID] += 1
        else:
            self.items[cuisineID] = 1
        self.size += 1
        return self.size

    def clear(self):
        self.items = {}
        self.size = 0

    @classmethod
    def fromjsons(cls, json_str):
        obj = cls()
        if json_str:
            jobj = json.loads(json_str)
            obj.items = jobj['items']
            obj.size = jobj['size']
        return obj

    def tojsons(self):
        return json.dumps({
            'items': self.items,
            'size': self.size,
        })
