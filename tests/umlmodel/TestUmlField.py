
from typing import List

from unittest import TestSuite

from unittest import main as unitTestMain

from copy import deepcopy

from tests.ProjectTestBase import ProjectTestBase

from umlmodel.Field import Field
from umlmodel.FieldType import FieldType
from umlmodel.UmlType import UmlType

from umlmodel.enumerations.Visibility import Visibility


class TestUmlField(ProjectTestBase):

    fieldNames:        List[str]       = ['field1', 'field2', 'field3']
    fieldTypes:        List[FieldType] = [FieldType(value='int'),
                                          FieldType(value='bool'),
                                          FieldType(value='float')
                                          ]
    fieldValues:       List[str]      = ['22', 'False', '62.34324']
    fieldVisibilities: List[Visibility] = [Visibility.PRIVATE,
                                           Visibility.PUBLIC,
                                           Visibility.PROTECTED
                                           ]

    def setUp(self):
        super().setUp()

    def testDeepCopyList(self):

        originalFields: List[Field] = []
        for x in range(len(TestUmlField.fieldNames)):
            field: Field = Field(name=TestUmlField.fieldNames[x],               # bug in pycharm, fixed in 2025.3
                                 type=TestUmlField.fieldTypes[x],
                                 defaultValue=TestUmlField.fieldValues[x],
                                 visibility=TestUmlField.fieldVisibilities[x]   # bug in pycharm, fixed in 2025.3
                                 )
            originalFields.append(field)
        self.logger.info(f'originalFields: {originalFields}')

        dopplegangers: List[Field] = deepcopy(originalFields)
        self.logger.info(f'{dopplegangers=}')

        for pyutField in dopplegangers:
            self.assertTrue(isinstance(pyutField.type, UmlType), 'Wrong type copied')
            self.assertTrue(isinstance(pyutField.visibility, Visibility), 'Wrong visibility type copied')

    def testBasicStringRepresentation(self):

        basicField: Field = Field(name='basicField',
                                  type=FieldType('int'),
                                  defaultValue='42',
                                  visibility=Visibility.PUBLIC)

        expectedValue: str = '+basicField: int = 42'
        actualValue:   str = basicField.__str__()

        self.assertEqual(expectedValue, actualValue, 'Basic string representation broken')

    def testNoDefaultValueStringRepresentation(self):

        noDefaultValueField: Field = Field(name='basicField',
                                           type=FieldType('int'),
                                           visibility=Visibility.PRIVATE)

        expectedValue: str = '-basicField: int'
        actualValue:   str = noDefaultValueField.__str__()

        self.assertEqual(expectedValue, actualValue, 'Basic string representation broken')


def suite() -> TestSuite:

    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestUmlField))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
