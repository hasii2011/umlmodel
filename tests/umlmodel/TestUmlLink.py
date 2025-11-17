
from unittest import TestSuite
from unittest import main as unitTestMain

from tests.ProjectTestBase import ProjectTestBase

from umlmodel.UmlLink import UmlLink

from umlmodel.UmlSDInstance import UmlSDInstance
from umlmodel.UmlSDMessage import UmlSDMessage

from umlmodel.enumerations.UmlLinkType import UmlLinkType


class TestUmlLink(ProjectTestBase):
    """
    """
    def setUp(self):
        super().setUp()
        # import warnings
        # To ignore this warning:
        # DeprecationWarning
        # Since this is legacy stuff;  May go away
        # warnings.simplefilter("ignore", category=DeprecationWarning)

    def tearDown(self):
        pass

    def testValidLinkType(self):

        pyutLink: UmlLink = UmlLink(name='ValidUmlLink')
        linkType: UmlLinkType = UmlLinkType.COMPOSITION

        pyutLink.linkType = linkType

        expectedLinkType: UmlLinkType = UmlLinkType.COMPOSITION
        actualLinkType:   UmlLinkType = pyutLink.linkType

        self.assertEqual(expectedLinkType, actualLinkType, 'Incorrect  valid legacy type support')

    def testLinkAssignment(self):

        sourceInstance:      UmlSDInstance = UmlSDInstance(instanceName='SourceInstance')
        destinationInstance: UmlSDInstance = UmlSDInstance(instanceName='DestinationInstance')

        message: UmlSDMessage = UmlSDMessage(message='callback')
        message.source      = sourceInstance
        message.destination = destinationInstance

        checkSource: UmlSDInstance = message.source
        self.assertIsNotNone(checkSource, 'Did we pass')


def suite() -> TestSuite:
    """You need to change the name of the test class here also."""
    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestUmlLink))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
