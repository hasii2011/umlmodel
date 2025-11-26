
from typing import ClassVar

from dataclasses import dataclass

from umlmodel.UmlModelBase import UmlModelBase


@dataclass
class Text(UmlModelBase):

    DEFAULT_TEXT: ClassVar[str] = 'Text to display'

    content: str = DEFAULT_TEXT
    """
    The model has to remember additional text attributes
    """
    def __init__(self, content: str = DEFAULT_TEXT):
        """

        Args:
            content: The text string to display
        """
        super().__init__()
        self.content = content
