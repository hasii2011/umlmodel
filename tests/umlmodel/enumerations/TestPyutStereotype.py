
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
        pyutStereotype: Stereotype = Stereotype.toEnum(Stereotype.TYPE.value)

        self.assertEqual(Stereotype.TYPE, pyutStereotype, 'Basic conversion failing')

    def testBasicNoStereotype(self):
        pyutStereotype: Stereotype = Stereotype.toEnum(Stereotype.NO_STEREOTYPE.value)

        self.assertEqual(Stereotype.NO_STEREOTYPE, pyutStereotype, 'Basic conversion failing')

    def testBasicNoImplementationClass(self):
        pyutStereotype: Stereotype = Stereotype.toEnum(Stereotype.IMPLEMENTATION_CLASS.value)

        self.assertEqual(Stereotype.IMPLEMENTATION_CLASS, pyutStereotype, 'Basic conversion failing')

    def testEmptyString(self):
        pyutStereotype: Stereotype = Stereotype.toEnum('')

        self.assertEqual(Stereotype.NO_STEREOTYPE, pyutStereotype, 'Empty string conversion failing')

    def testNone(self):
        pyutStereotype: Stereotype = Stereotype.toEnum(cast(str, None))

        self.assertEqual(Stereotype.NO_STEREOTYPE, pyutStereotype, 'Empty string conversion failing')

    def testManySpaces(self):
        pyutStereotype: Stereotype = Stereotype.toEnum('    ')

        self.assertEqual(Stereotype.NO_STEREOTYPE, pyutStereotype, 'Empty string conversion failing')

    def testInvalidStereotypeCoercionToNoStereotype(self):

        pyutStereotype: Stereotype = Stereotype.toEnum('dataclass')

        self.assertEqual(Stereotype.NO_STEREOTYPE, pyutStereotype, 'Coerced to empty')

    def testUpperCaseValidValue(self):
        pyutStereotype: Stereotype = Stereotype.toEnum('SPECIFICATION')

        self.assertEqual(Stereotype.SPECIFICATION, pyutStereotype, 'Coerced to empty')

    def testNodeTypeEnum(self):
        pyutStereotype: Stereotype = Stereotype.toEnum('NODE type')

        self.assertEqual(Stereotype.NODE_TYPE, pyutStereotype, 'Coerced to empty')


def suite() -> TestSuite:
    """You need to change the name of the test class here also."""
    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestUmlStereotype))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
