
from unittest import TestSuite
from unittest import main as unitTestMain

from copy import deepcopy

from tests.ProjectTestBase import ProjectTestBase
from umlmodel.UmlInterface import UmlInterface


class TestUmlInterface(ProjectTestBase):
    """
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def testInstantiation(self):

        pyutInterface: UmlInterface = UmlInterface(name='OzzeeInterface')

        self.assertIsNotNone(pyutInterface.implementors, 'Ensure we can access this property')

    def testEquality(self):
        pyutInterface: UmlInterface = UmlInterface(name='OzzeeInterface')
        doppleGanger:  UmlInterface = deepcopy(pyutInterface)

        self.assertTrue(pyutInterface == doppleGanger, 'Should be the same one')

    def testNotEqual(self):

        pyutInterface1: UmlInterface = UmlInterface(name='OzzeeInterface')
        pyutInterface2: UmlInterface = UmlInterface(name='OzzeeInterface')

        self.assertFalse(pyutInterface1 == pyutInterface2, 'IDs should not match')


def suite() -> TestSuite:
    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestUmlInterface))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
