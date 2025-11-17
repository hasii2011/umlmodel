
from unittest import TestSuite
from unittest import main as unitTestMain

from umlmodel.UmlObject import UmlObject
from umlmodel.UmlObject import infiniteSequence

from tests.ProjectTestBase import ProjectTestBase


class TestUmlObject(ProjectTestBase):
    """
    """
    def setUp(self):

        super().setUp()
        UmlObject.idGenerator = infiniteSequence()

    def tearDown(self):
        pass

    def testNoName(self):
        umlObject: UmlObject = UmlObject()

        expectedSize: int = 0
        actualSize:   int = umlObject.name.__len__()

        self.assertEqual(expectedSize, actualSize, 'Name should be empty')

    def testNoNameValue(self):

        umlObject: UmlObject = UmlObject()

        actualName:     str = umlObject.name

        self.assertIsNotNone(actualName, 'Should have some value')

        expectedLength: int = 0
        actualLength:   int = len(actualName)

        self.assertEqual(expectedLength, actualLength, 'Should be empty')

    def testProvidedName(self):

        providedName: str = 'El Gato Malo'
        nameLength:   int = len(providedName)

        umlObject: UmlObject = UmlObject(providedName)

        expectedLength: int = nameLength
        actualLength:   int = len(umlObject.name)

        self.assertEqual(expectedLength, actualLength, 'Our name appears to have NOT been used')

    def testHowIdsIncrement(self):

        umlObject1: UmlObject = UmlObject(name='umlObject1')
        self.assertEqual(0, umlObject1.id, f'{umlObject1.name} - Incorrect id')

        umlObject2: UmlObject = UmlObject(name='umlObject2')
        self.assertEqual(1, umlObject2.id, f'{umlObject2.name} - Incorrect id')

        umlObject3: UmlObject = UmlObject(name='umlObject3')
        self.assertEqual(2, umlObject3.id, f'{umlObject3.name} - Incorrect id')


def suite() -> TestSuite:
    """You need to change the name of the test class here also."""
    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestUmlObject))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
