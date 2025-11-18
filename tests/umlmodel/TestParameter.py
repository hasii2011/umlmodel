
from unittest import TestSuite
from unittest import main as unitTestMain

from tests.ProjectTestBase import ProjectTestBase
from umlmodel.Parameter import Parameter

from umlmodel.UmlType import UmlType


class TestParameter(ProjectTestBase):
    """
    """
    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def testFullString(self):
        umlParameter: Parameter = Parameter(name='Ozzee', type=UmlType('float'), defaultValue='1.0')

        expectedValue: str = 'Ozzee: float = 1.0'
        actualValue:   str = umlParameter.__str__()

        self.assertEqual(expectedValue, actualValue, 'Full string representation has changed')

    def testIndividualAttributes(self):
        umlParameter: Parameter = Parameter(name='Ozzee', type=UmlType('float'), defaultValue='1.0')

        self.assertEqual('Ozzee', umlParameter.name, 'Parameter name not correct')
        self.assertEqual('1.0', umlParameter.defaultValue, 'default value not set correctly')
        self.assertEqual(UmlType('float'), umlParameter.type, 'Type not set correctly')

    def testNoDefaultValue(self):
        umlParameter: Parameter = Parameter(name='Ozzee', type=UmlType('float'))

        expectedValue: str = 'Ozzee: float'
        actualValue:   str = umlParameter.__str__()

        self.assertEqual(expectedValue, actualValue, 'No default value string representation has changed')

    def testNoTypeOrDefaultValue(self):

        umlParameter: Parameter = Parameter(name='Ozzee')

        expectedValue: str = 'Ozzee'
        actualValue:   str = umlParameter.__str__()

        self.assertEqual(expectedValue, actualValue, 'No Type, no default value string representation has changed')

    def testDataClassRepr(self):

        umlParameter: Parameter = Parameter(name='Ozzee', type=UmlType('float'), defaultValue='1.0')

        expectedValue: str = 'Ozzee: float = 1.0'
        actualValue:   str = umlParameter.__repr__()

        self.assertEqual(expectedValue, actualValue, 'Full string representation has changed')


def suite() -> TestSuite:
    """You need to change the name of the test class here also."""
    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestParameter))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
