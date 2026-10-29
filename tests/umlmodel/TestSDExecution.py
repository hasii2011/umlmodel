
from unittest import TestSuite
from unittest import main as unitTestMain

from tests.ProjectTestBase import ProjectTestBase
from umlmodel.SDExecution import SDExecution
from umlmodel.SDInstance import SDInstance
from umlmodel.SDMessage import SDMessage


class TestSDExecution(ProjectTestBase):
    """
    Unit tests for the SDExecution model class.
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def testDefaultProperties(self):
        """
        Verify that default values for optional coordinates, messages, and base attributes are set properly.
        """
        sampleInstance:  SDInstance = SDInstance(instanceName='ServerLifeline')
        pyutSDExecution: SDExecution = SDExecution(instance=sampleInstance)

        self.assertEqual(sampleInstance, pyutSDExecution.instance, 'Instance should match provided SDInstance')
        self.assertEqual(0, pyutSDExecution.startTime, 'Default startTime should be 0')
        self.assertEqual(0, pyutSDExecution.endTime, 'Default endTime should be 0')
        self.assertEqual(0, pyutSDExecution.nestingLevel, 'Default nestingLevel should be 0')
        self.assertIsNone(pyutSDExecution.operation, 'Default operation should be None')
        self.assertIsNone(pyutSDExecution.startMessage, 'Default startMessage should be None')
        self.assertIsNone(pyutSDExecution.finishMessage, 'Default finishMessage should be None')

        self.assertEqual('', pyutSDExecution.name, 'Default name should be empty')
        self.assertEqual('', pyutSDExecution.fileName, 'Default fileName should be empty')
        self.assertTrue(len(pyutSDExecution.id) > 0, 'Unique ID should be generated upon post-init')

    def testPositionalInstantiation(self):
        """
        Verify that SDExecution can be instantiated positionally with mandatory instance argument.
        """
        sampleInstance:  SDInstance  = SDInstance(instanceName='ClientLifeline')
        pyutSDExecution: SDExecution = SDExecution(sampleInstance)

        self.assertEqual(sampleInstance, pyutSDExecution.instance, 'Positional instance should be bound')

    def testExplicitProperties(self):
        """
        Verify setting explicit coordinates, operations, and nested levels.
        """
        sampleInstance:       SDInstance = SDInstance(instanceName='DatabaseLifeline')
        expectedStartTime:    int = 25
        expectedEndTime:      int = 150
        expectedNestingLevel: int = 2
        expectedOperation:    str = 'queryRecords'

        pyutSDExecution: SDExecution = SDExecution(
            instance=sampleInstance,
            startTime=expectedStartTime,
            endTime=expectedEndTime,
            nestingLevel=expectedNestingLevel,
            operation=expectedOperation,
        )

        self.assertEqual(expectedStartTime, pyutSDExecution.startTime, 'startTime should match')
        self.assertEqual(expectedEndTime, pyutSDExecution.endTime, 'endTime should match')
        self.assertEqual(expectedNestingLevel, pyutSDExecution.nestingLevel, 'nestingLevel should match')
        self.assertEqual(expectedOperation, pyutSDExecution.operation, 'operation should match')

    def testWithMessages(self):
        """
        Verify binding start and finish messages to the execution specification.
        """
        targetInstance: SDInstance = SDInstance(instanceName='Callee')

        startMessage:  SDMessage = SDMessage(message='executeRequest')
        finishMessage: SDMessage = SDMessage(message='returnReply')

        pyutSDExecution: SDExecution = SDExecution(
            instance=targetInstance,
            startMessage=startMessage,
            finishMessage=finishMessage,
        )

        self.assertEqual(startMessage, pyutSDExecution.startMessage, 'startMessage should match')
        self.assertEqual(finishMessage, pyutSDExecution.finishMessage, 'finishMessage should match')


def suite() -> TestSuite:
    """
    Builds the test suite for TestSDExecution.
    """
    import unittest

    testSuite: TestSuite = TestSuite()
    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestSDExecution))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
