
from typing import List

from unittest import main as unitTestMain
from unittest import TestSuite

from copy import deepcopy

from tests.ProjectTestBase import ProjectTestBase
from umlmodel.ReturnType import ReturnType


class TestReturnType(ProjectTestBase):

    def setUp(self):
        super().setUp()

    def testDeepCopyReturnType(self):

        typeValues:    List[str]      = ['int', 'bool', 'float']
        originalTypes: List[ReturnType] = []

        for aValue in typeValues:
            returnType: ReturnType = ReturnType(value=aValue)
            originalTypes.append(returnType)
        self.logger.info(f'{originalTypes=}')

        # noinspection SpellCheckingInspection
        doppleGangers: List[ReturnType] = deepcopy(originalTypes)

        # noinspection SpellCheckingInspection
        self.logger.info(f'{doppleGangers=}')

        self.assertIn(member=originalTypes[0], container=doppleGangers, msg='')
        self.assertIn(member=originalTypes[1], container=doppleGangers, msg='')
        self.assertIn(member=originalTypes[2], container=doppleGangers, msg='')


def suite() -> TestSuite:

    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestReturnType))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
