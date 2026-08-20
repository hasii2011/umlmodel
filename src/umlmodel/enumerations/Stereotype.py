
from typing import Optional
from typing import cast
from enum import Enum


class Stereotype(Enum):
    """
    Stereotype Enumeration
    https://www.ibm.com/docs/en/rational-soft-arch/9.5?topic=elements-uml-model-element-stereotypes
    """
    AUXILIARY            = 'auxiliary'
    BOUNDARY             = 'boundary'
    BUILD_COMPONENT      = 'buildComponent'
    CONTROL              = 'control'
    DOCUMENT             = 'document'
    ENTITY               = 'entity'
    EXECUTABLE           = 'executable'
    FILE                 = 'file'
    FOCUS                = 'focus'
    IMPLEMENT            = 'implement'
    IMPLEMENTATION_CLASS = 'implementationClass'
    INTERFACE            = 'interface'
    LIBRARY              = 'library'
    METACLASS            = 'metaclass'
    NODE_TYPE            = 'node type'
    # noinspection SpellCheckingInspection
    POWER_TYPE           = 'powertype'
    REALIZATION          = 'realization'
    SCRIPT               = 'script'
    SERVICE              = 'service'
    SOURCE               = 'source'
    SPECIFICATION        = 'specification'
    SUBSYSTEM            = 'subsystem'
    THREAD               = 'thread'
    TYPE                 = 'type'
    UTILITY              = 'utility'
    ENUMERATION          = 'enumeration'
    NO_STEREOTYPE        = 'noStereotype'

    @classmethod
    def toEnum(cls, strValue: Optional[str]) -> 'Stereotype':
        """
        Converts the input string to the appropriate stereotype

        Args:
            strValue:   A string value

        Returns:  The stereotype enumeration;  Empty strings, multi-spaces strings,
        invalid & None values return Stereotype.NO_STEREOTYPE
        """
        if strValue is None:
            return cls.NO_STEREOTYPE

        canonicalStr: str = strValue.strip(' ').lower()
        if not canonicalStr:
            return cls.NO_STEREOTYPE

        for member in cls:
            memberVal: Stereotype = cast(Stereotype, member)
            if memberVal.value.lower() == canonicalStr or memberVal.name.lower() == canonicalStr:
                return memberVal

        return cls.NO_STEREOTYPE
