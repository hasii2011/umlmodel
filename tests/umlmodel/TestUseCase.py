
from unittest import TestSuite
from unittest import main as unitTestMain

from tests.ProjectTestBase import ProjectTestBase

from umlmodel.UseCase import UseCase


class TestUseCase(ProjectTestBase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def testInstantiation(self):
        pyutUseCase: UseCase = UseCase(name='Ozzee')

        self.assertIsNotNone(pyutUseCase, 'Wowza, I made it')

    def testInstantiationNoName(self):
        pyutUseCase: UseCase = UseCase()

        self.assertIsNotNone(pyutUseCase, 'Wowza, I made it')


def suite() -> TestSuite:
    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestUseCase))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
