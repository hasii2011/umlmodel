
from unittest import TestSuite
from unittest import main as unitTestMain

from tests.ProjectTestBase import ProjectTestBase
from umlmodel.UmlMethod import SourceCode
from umlmodel.UmlMethod import UmlMethod
from umlmodel.UmlMethod import UmlParameters
from umlmodel.UmlParameter import UmlParameter
from umlmodel.UmlType import UmlType


class TestUmlMethod(ProjectTestBase):
    """
    """
    def setUp(self):
        super().setUp()
        self._pyutMethod: UmlMethod = UmlMethod(name='methodName')

    def tearDown(self):
        pass

    def testUpdateEmptyParameters(self):

        pyutMethod:    UmlMethod    = UmlMethod(name='MethodToBuildUp')
        pyutParameter: UmlParameter = UmlParameter(name='InitialParameter')

        pyutMethod.addParameter(parameter=pyutParameter)

        self.assertEqual(1, len(pyutMethod.parameters), "There can be only one")

    def testStringMethodWithParametersRepresentation(self):

        pyutMethod: UmlMethod = self._pyutMethod
        pyutMethod.returnType = UmlType('float')

        pyutMethod.parameters = self._makeParameters()

        defaultName:            str = 'methodName'
        expectedRepresentation: str = f'+{defaultName}(intParam: int = 0, floatParam: float = 32.0): float'
        actualRepresentation:   str = pyutMethod.methodWithParameters()

        self.assertEqual(expectedRepresentation, actualRepresentation, 'Oops this does not match')

    def testStringMethodWithoutParametersRepresentation(self):

        pyutMethod:     UmlMethod = self._pyutMethod
        pyutMethod.returnType = UmlType('float')

        pyutMethod.parameters = self._makeParameters()

        defaultName:            str = 'methodName'
        expectedRepresentation: str = f'+{defaultName}(): float'
        actualRepresentation:   str = pyutMethod.methodWithoutParameters()

        self.assertEqual(expectedRepresentation, actualRepresentation, 'Oops this does not match')

    def testMethodSimpleParametersWithParameters(self):
        simpleMethod: UmlMethod = self._pyutMethod

        simpleMethod.parameters = self._makeSimpleParameters()

        defaultName: str = 'methodName'
        expectedRepresentation: str = (
            f'+{defaultName}('
            f'{simpleMethod.parameters[0].name}, '
            f'{simpleMethod.parameters[1].name}, '
            f'{simpleMethod.parameters[2].name}'
            ')'
        )
        actualRepresentation:   str = simpleMethod.methodWithParameters()

        self.assertEqual(expectedRepresentation, actualRepresentation, 'Simple Method Simple Parameters does not match')

    def testStashSourceCode(self):

        pyutMethod:        UmlMethod = self._generateAMethod()
        expectedLineCount: int = 5
        actualLineCount:   int = len(pyutMethod.sourceCode)
        self.assertEqual(expectedLineCount, actualLineCount, 'Method source code not accurate')

    def testChangeSourceCode(self):
        pyutMethod:        UmlMethod = self._generateAMethod()
        #
        # This is NOT the recommended way to update the source code
        #
        pyutMethod.sourceCode.insert(2, '# I am a comment')
        expectedLineCount: int = 6
        actualLineCount:   int = len(pyutMethod.sourceCode)
        self.assertEqual(expectedLineCount, actualLineCount, 'Method source code not accurate')

    def _generateAMethod(self) -> UmlMethod:
        pyutMethod: UmlMethod    = UmlMethod(name='OzzeeElGatoDiablo')

        pyutMethod.sourceCode = SourceCode(
            [
                'weLeft:           bool = True',
                'isOzzeeAGoodGato: bool = False',
                'if weLeft is True:',
                '    isOzzeeAGoodGato = True',
                'return isOzzeeAGoodGato'
            ]
        )
        return pyutMethod

    def _makeParameters(self) -> UmlParameters:

        pyutParameter1: UmlParameter  = UmlParameter(name='intParam', type=UmlType("int"), defaultValue='0')
        pyutParameter2: UmlParameter  = UmlParameter(name='floatParam', type=UmlType("float"), defaultValue='32.0')
        parameters:     UmlParameters = UmlParameters([pyutParameter1, pyutParameter2])

        return parameters

    def _makeSimpleParameters(self) -> UmlParameters:
        """
        No types, no default values
        """
        intParameter:   UmlParameter  = UmlParameter(name='intParameter')
        floatParameter: UmlParameter  = UmlParameter(name='floatParameter')
        boolParameter:  UmlParameter  = UmlParameter(name='boolParameter')

        parameters:     UmlParameters = UmlParameters([intParameter, floatParameter, boolParameter])

        return parameters


def suite() -> TestSuite:

    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestUmlMethod))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
