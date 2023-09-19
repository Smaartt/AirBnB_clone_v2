#!/usr/bin/python3
"""
Module cCity class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    It Inherits from BaseModel
    Public class attributes:
        state_id: (str) will be State.id
        name:     (str)
    """
    state_id = ""
    name = ""
