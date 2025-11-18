
from unittest import TestSuite
from unittest import main as unitTestMain

from tests.ProjectTestBase import ProjectTestBase
from umlmodel.Method import SourceCode
from umlmodel.Method import Method
from umlmodel.Method import Parameters

from umlmodel.Parameter import Parameter
from umlmodel.ParameterType import ParameterType

from umlmodel.ReturnType import ReturnType

from umlmodel.UmlType import UmlType


class TestUmlMethod(ProjectTestBase):
    """
    """
    def setUp(self):
        super().setUp()
        self._pyutMethod: Method = Method(name='methodName')

    def tearDown(self):
        pass

    def testUpdateEmptyParameters(self):

        pyutMethod:    Method    = Method(name='MethodToBuildUp')
        pyutParameter: Parameter = Parameter(name='InitialParameter')

        pyutMethod.addParameter(parameter=pyutParameter)

        self.assertEqual(1, len(pyutMethod.parameters), "There can be only one")

    def testStringMethodWithParametersRepresentation(self):

        method: Method = self._pyutMethod
        method.returnType = ReturnType('float')

        method.parameters = self._makeParameters()

        defaultName:            str = 'methodName'
        expectedRepresentation: str = f'+{defaultName}(intParam: int = 0, floatParam: float = 32.0): float'
        actualRepresentation:   str = method.methodWithParameters()

        self.assertEqual(expectedRepresentation, actualRepresentation, 'Oops this does not match')

    def testStringMethodWithoutParametersRepresentation(self):

        method: Method = self._pyutMethod
        method.returnType = ReturnType('float')

        method.parameters = self._makeParameters()

        defaultName:            str = 'methodName'
        expectedRepresentation: str = f'+{defaultName}(): float'
        actualRepresentation:   str = method.methodWithoutParameters()

        self.assertEqual(expectedRepresentation, actualRepresentation, 'Oops this does not match')

    def testMethodSimpleParametersWithParameters(self):
        simpleMethod: Method = self._pyutMethod

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

        method:            Method = self._generateAMethod()
        expectedLineCount: int = 5
        actualLineCount:   int = len(method.sourceCode)
        self.assertEqual(expectedLineCount, actualLineCount, 'Method source code not accurate')

    def testChangeSourceCode(self):

        method: Method = self._generateAMethod()
        #
        # This is NOT the recommended way to update the source code
        #
        method.sourceCode.insert(2, '# I am a comment')
        expectedLineCount: int = 6
        actualLineCount:   int = len(method.sourceCode)
        self.assertEqual(expectedLineCount, actualLineCount, 'Method source code not accurate')

    def _generateAMethod(self) -> Method:

        method: Method = Method(name='OzzeeElGatoDiablo')

        method.sourceCode = SourceCode(
            [
                'weLeft:           bool = True',
                'isOzzeeAGoodGato: bool = False',
                'if weLeft is True:',
                '    isOzzeeAGoodGato = True',
                'return isOzzeeAGoodGato'
            ]
        )
        return method

    def _makeParameters(self) -> Parameters:

        parameter1: Parameter  = Parameter(name='intParam',   type=ParameterType("int"), defaultValue='0')
        parameter2: Parameter  = Parameter(name='floatParam', type=ParameterType("float"), defaultValue='32.0')
        parameters:     Parameters = Parameters([parameter1, parameter2])

        return parameters

    def _makeSimpleParameters(self) -> Parameters:
        """
        No types, no default values
        """
        intParameter:   Parameter  = Parameter(name='intParameter')
        floatParameter: Parameter  = Parameter(name='floatParameter')
        boolParameter:  Parameter  = Parameter(name='boolParameter')

        parameters:     Parameters = Parameters([intParameter, floatParameter, boolParameter])

        return parameters


def suite() -> TestSuite:

    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestUmlMethod))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
