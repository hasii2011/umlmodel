
from typing import cast

from unittest import TestSuite
from unittest import main as unitTestMain


from tests.ProjectTestBase import ProjectTestBase
from umlmodel.enumerations.UmlStereotype import UmlStereotype


class TestUmlStereotype(ProjectTestBase):
    """
    """
    def setUp(self):
        super().setUp()

    def tearDown(self):
        pass

    def testBasic(self):
        pyutStereotype: UmlStereotype = UmlStereotype.toEnum(UmlStereotype.TYPE.value)

        self.assertEqual(UmlStereotype.TYPE, pyutStereotype, 'Basic conversion failing')

    def testBasicNoStereotype(self):
        pyutStereotype: UmlStereotype = UmlStereotype.toEnum(UmlStereotype.NO_STEREOTYPE.value)

        self.assertEqual(UmlStereotype.NO_STEREOTYPE, pyutStereotype, 'Basic conversion failing')

    def testBasicNoImplementationClass(self):
        pyutStereotype: UmlStereotype = UmlStereotype.toEnum(UmlStereotype.IMPLEMENTATION_CLASS.value)

        self.assertEqual(UmlStereotype.IMPLEMENTATION_CLASS, pyutStereotype, 'Basic conversion failing')

    def testEmptyString(self):
        pyutStereotype: UmlStereotype = UmlStereotype.toEnum('')

        self.assertEqual(UmlStereotype.NO_STEREOTYPE, pyutStereotype, 'Empty string conversion failing')

    def testNone(self):
        pyutStereotype: UmlStereotype = UmlStereotype.toEnum(cast(str, None))

        self.assertEqual(UmlStereotype.NO_STEREOTYPE, pyutStereotype, 'Empty string conversion failing')

    def testManySpaces(self):
        pyutStereotype: UmlStereotype = UmlStereotype.toEnum('    ')

        self.assertEqual(UmlStereotype.NO_STEREOTYPE, pyutStereotype, 'Empty string conversion failing')

    def testInvalidStereotypeCoercionToNoStereotype(self):

        pyutStereotype: UmlStereotype = UmlStereotype.toEnum('dataclass')

        self.assertEqual(UmlStereotype.NO_STEREOTYPE, pyutStereotype, 'Coerced to empty')

    def testUpperCaseValidValue(self):
        pyutStereotype: UmlStereotype = UmlStereotype.toEnum('SPECIFICATION')

        self.assertEqual(UmlStereotype.SPECIFICATION, pyutStereotype, 'Coerced to empty')

    def testNodeTypeEnum(self):
        pyutStereotype: UmlStereotype = UmlStereotype.toEnum('NODE type')

        self.assertEqual(UmlStereotype.NODE_TYPE, pyutStereotype, 'Coerced to empty')


def suite() -> TestSuite:
    """You need to change the name of the test class here also."""
    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestUmlStereotype))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
