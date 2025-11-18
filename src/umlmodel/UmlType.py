
from dataclasses import dataclass


@dataclass(frozen=True)
class UmlType:
    """
    How method and return types are represented
    """
    value: str = ''

    def __str__(self) -> str:
        """
        String representation.
        """
        return self.value
