
from enum import Enum

from dataclasses import dataclass

from umlmodel.UmlModelBase import UmlModelBase


class SDInstanceType(Enum):
    INSTANCE_TYPE_ACTOR = 'Actor'
    INSTANCE_TYPE_CLASS = 'Class'


@dataclass
class SDInstance(UmlModelBase):
    """
    Data model representation of a UML Collaboration instance.

    Maintains properties for the instance name, lifeline length, and its graphical
    representation type (e.g., Actor or Class).
    """
    instanceName:           str = 'Unnamed instance'
    instanceLifeLineLength: int = 200
    instanceGraphicalType:  SDInstanceType = SDInstanceType.INSTANCE_TYPE_CLASS
