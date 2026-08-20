
from typing import cast

from unittest import TestSuite
from unittest import main as unitTestMain


from tests.ProjectTestBase import ProjectTestBase
from umlmodel.enumerations.Stereotype import Stereotype


class TestUmlStereotype(ProjectTestBase):
    """
    """
    def setUp(self):
        super().setUp()

    def tearDown(self):
        pass

    def testBasic(self):
        stereotype: Stereotype = Stereotype.toEnum(Stereotype.TYPE.value)

        self.assertEqual(Stereotype.TYPE, stereotype, 'Basic conversion failing')

    def testBasicNoStereotype(self):
        stereotype: Stereotype = Stereotype.toEnum(Stereotype.NO_STEREOTYPE.value)

        self.assertEqual(Stereotype.NO_STEREOTYPE, stereotype, 'Basic conversion failing')

    def testBasicNoImplementationClass(self):
        stereotype: Stereotype = Stereotype.toEnum(Stereotype.IMPLEMENTATION_CLASS.value)

        self.assertEqual(Stereotype.IMPLEMENTATION_CLASS, stereotype, 'Basic conversion failing')

    def testEmptyString(self):
        stereotype: Stereotype = Stereotype.toEnum('')

        self.assertEqual(Stereotype.NO_STEREOTYPE, stereotype, 'Empty string conversion failing')

    def testNone(self):
        stereotype: Stereotype = Stereotype.toEnum(cast(str, None))

        self.assertEqual(Stereotype.NO_STEREOTYPE, stereotype, 'Empty string conversion failing')

    def testManySpaces(self):
        stereotype: Stereotype = Stereotype.toEnum('    ')

        self.assertEqual(Stereotype.NO_STEREOTYPE, stereotype, 'Empty string conversion failing')

    def testInvalidStereotypeCoercionToNoStereotype(self):

        stereotype: Stereotype = Stereotype.toEnum('dataclass')

        self.assertEqual(Stereotype.NO_STEREOTYPE, stereotype, 'Coerced to empty')

    def testUpperCaseValidValue(self):
        stereotype: Stereotype = Stereotype.toEnum('SPECIFICATION')

        self.assertEqual(Stereotype.SPECIFICATION, stereotype, 'Coerced to empty')

    def testNodeTypeEnum(self):
        stereotype: Stereotype = Stereotype.toEnum('NODE type')

        self.assertEqual(Stereotype.NODE_TYPE, stereotype, 'Coerced to empty')

    def testMetaClassAllUpper(self):
        stereotype: Stereotype = Stereotype.toEnum('METACLASS')
        self.assertEqual(Stereotype.METACLASS, stereotype, 'Canonicalization not working')

    def testStereotypeEnumeration(self):
        stereotype: Stereotype = Stereotype.toEnum('enumeration')
        self.assertEqual(Stereotype.ENUMERATION, stereotype, 'Canonicalization not working')


def suite() -> TestSuite:
    """You need to change the name of the test class here also."""
    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestUmlStereotype))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
