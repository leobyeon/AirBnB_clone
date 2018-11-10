#!/usr/bin/python3
"""Class BaseModel - defines all common attributes/methods for other classes"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Class BaseModel -
    """
    def __init__(self, *args, **kwargs):
        """func __init__ - no args"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for k, v in kwargs.items():
                if k == "created_at":
                    v = datetime.now()
                if k == "updated_at":
                    v = datetime.now()
                if k != "__class__":
                    self.__setattr__(k, v)

    def __str__(self):
        """func __str__ - no args"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """func save - no args"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """func to_dict - kwargs"""
        d = self.__dict__
        d["__class__"] = self.__class__.__name__
        for k, v in d.items():
            d[k] = v
            if k == "created_at" or k == "updated_at":
                d[k] = v.isoformat()
        return (d)
