
from unittest import TestSuite
from unittest import main as unitTestMain

from tests.ProjectTestBase import ProjectTestBase

from umlmodel.Link import Link

from umlmodel.SDInstance import SDInstance
from umlmodel.SDMessage import SDMessage

from umlmodel.enumerations.LinkType import LinkType


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

        pyutLink: Link = Link(name='ValidUmlLink')
        linkType: LinkType = LinkType.COMPOSITION

        pyutLink.linkType = linkType

        expectedLinkType: LinkType = LinkType.COMPOSITION
        actualLinkType:   LinkType = pyutLink.linkType

        self.assertEqual(expectedLinkType, actualLinkType, 'Incorrect  valid legacy type support')

    def testLinkAssignment(self):

        sourceInstance:      SDInstance = SDInstance(instanceName='SourceInstance')
        destinationInstance: SDInstance = SDInstance(instanceName='DestinationInstance')

        message: SDMessage = SDMessage(message='callback')
        message.source      = sourceInstance
        message.destination = destinationInstance

        checkSource: SDInstance = message.source
        self.assertIsNotNone(checkSource, 'Did we pass')


def suite() -> TestSuite:
    """You need to change the name of the test class here also."""
    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestUmlLink))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
