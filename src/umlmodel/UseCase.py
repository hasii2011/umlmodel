
from dataclasses import dataclass

from umlmodel.LinkedObject import LinkedObject


@dataclass
class UseCase(LinkedObject):
    """
    Represents a Use Case within a UML Use Case Diagram.

    Inherits from LinkedObject to enable linking with other diagram
    components such as actors.
    """
    def __init__(self, name: str = ''):

        super().__init__(name=name)
