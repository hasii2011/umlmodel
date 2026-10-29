
from typing import Optional

from dataclasses import dataclass

from umlmodel.SDInstance import SDInstance
from umlmodel.SDMessage import SDMessage
from umlmodel.UmlModelBase import UmlModelBase


@dataclass
class SDExecution(UmlModelBase):

    instance:      SDInstance
    startTime:     int                  = 0
    endTime:       int                  = 0
    nestingLevel:  int                  = 0
    operation:     Optional[str]        = None
    startMessage:  Optional[SDMessage]  = None
    finishMessage: Optional[SDMessage]  = None
