
from unittest import TestSuite
from unittest import main as unitTestMain

from umlmodel.UmlModelBase import UmlModelBase
from umlmodel.UmlModelBase import uniqueIdentifier

from tests.ProjectTestBase import ProjectTestBase


class TestUmlBase(ProjectTestBase):
    """
    """
    def setUp(self):

        super().setUp()
        UmlModelBase.idGenerator = uniqueIdentifier()

    def tearDown(self):
        pass

    def testNoName(self):
        umlObject: UmlModelBase = UmlModelBase()

        expectedSize: int = 0
        actualSize:   int = umlObject.name.__len__()

        self.assertEqual(expectedSize, actualSize, 'Name should be empty')

    def testNoNameValue(self):

        umlObject: UmlModelBase = UmlModelBase()

        actualName:     str = umlObject.name

        self.assertIsNotNone(actualName, 'Should have some value')

        expectedLength: int = 0
        actualLength:   int = len(actualName)

        self.assertEqual(expectedLength, actualLength, 'Should be empty')

    def testProvidedName(self):

        providedName: str = 'El Gato Malo'
        nameLength:   int = len(providedName)

        umlObject: UmlModelBase = UmlModelBase(providedName)

        expectedLength: int = nameLength
        actualLength:   int = len(umlObject.name)

        self.assertEqual(expectedLength, actualLength, 'Our name appears to have NOT been used')


def suite() -> TestSuite:
    """You need to change the name of the test class here also."""
    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestUmlBase))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
