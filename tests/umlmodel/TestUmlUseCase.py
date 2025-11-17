
from unittest import TestSuite
from unittest import main as unitTestMain

from tests.ProjectTestBase import ProjectTestBase

from umlmodel.UmlUseCase import UmlUseCase


class TestUmlCase(ProjectTestBase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def testInstantiation(self):
        pyutUseCase: UmlUseCase = UmlUseCase(name='Ozzee')

        self.assertIsNotNone(pyutUseCase, 'Wowza, I made it')

    def testInstantiationNoName(self):
        pyutUseCase: UmlUseCase = UmlUseCase()

        self.assertIsNotNone(pyutUseCase, 'Wowza, I made it')


def suite() -> TestSuite:
    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestUmlCase))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
