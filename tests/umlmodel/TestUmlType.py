
from typing import List

from unittest import main as unitTestMain
from unittest import TestSuite

from copy import deepcopy

from tests.ProjectTestBase import ProjectTestBase
from umlmodel.UmlType import UmlType


class TestUmlType(ProjectTestBase):

    def setUp(self):
        super().setUp()

    def testDeepCopyPyutTypes(self):

        typeValues:    List[str]      = ['int', 'bool', 'float']
        originalTypes: List[UmlType] = []

        for aValue in typeValues:
            pyutType: UmlType = UmlType(value=aValue)
            originalTypes.append(pyutType)
        self.logger.info(f'{originalTypes=}')

        # noinspection SpellCheckingInspection
        doppleGangers: List[UmlType] = deepcopy(originalTypes)

        # noinspection SpellCheckingInspection
        self.logger.info(f'{doppleGangers=}')

        self.assertIn(member=originalTypes[0], container=doppleGangers, msg='')
        self.assertIn(member=originalTypes[1], container=doppleGangers, msg='')
        self.assertIn(member=originalTypes[2], container=doppleGangers, msg='')


def suite() -> TestSuite:

    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestUmlType))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
