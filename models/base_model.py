#!/usr/bin/python3
"""This script is a base model"""

import uuid
from datetime import datetime
from models import storage

class Basemodels:
    """Class from which other classes will inherit"""
    
    def __init__(self, *args, **kwargs):
        """initialization instance attributes

        Args:
            _*args: list of arguments
            _**kwargs: dict of keys_values arguments
        """

        if kwargs is not  None and kwargs !={}:
            for key in kwargs:
                if key == "creatyed_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
            else:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
                storage.new(self)

        def __str__(self):
            """update the public instance attribute updated_at"""

            self.update_at = datetime.now()
            storage.save()

        def to_dict(self):
            """returns a dictionary containing all keys/values of __dict__"""
            my_dict = self.__dict__.copy()
            my_dict["__class__"] = type(self).__name__
            my_dict["created_at"] =my_dict["created_at"].isoformat()
            my_dict["updated_at"] = my_dict["updated_at"].isoformat()
            return my_dict



