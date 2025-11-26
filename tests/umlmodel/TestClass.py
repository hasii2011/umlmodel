
from unittest import TestSuite
from unittest import main as unitTestMain

from tests.ProjectTestBase import ProjectTestBase

from umlmodel.Class import Class
from umlmodel.LinkedObject import LinkedObject
from umlmodel.UmlModelBase import UmlModelBase
from umlmodel.UmlModelBase import uniqueIdentifier

from umlmodel.enumerations.DisplayParameters import DisplayParameters
from umlmodel.enumerations.Stereotype import Stereotype


class TestClass(ProjectTestBase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def testMultipleInheritance(self):

        pyutClass: Class = Class(name='')
        self.logger.info(f'{len(pyutClass.fields)=}')

    def testLinksAndParent(self):

        pyutClass: Class = Class(name='CheckLinks')
        self.assertTrue(len(pyutClass.parents) == 0, 'No parents at instantiation')
        self.assertTrue(len(pyutClass.links) == 0, 'No links at instantiation')

    def testBasicPropertiesDisplayParameters(self):

        pyutClass: Class = Class(name='CheckDisplayProperties')
        self.assertEqual(DisplayParameters.UNSPECIFIED, pyutClass.displayParameters)

    def testBasicPropertiesStereotype(self):

        pyutClass: Class = Class(name='CheckStereotype')
        self.assertEqual(Stereotype.NO_STEREOTYPE, pyutClass.stereotype)

    def testBasicPropertiesDisplayStereotype(self):

        pyutClass: Class = Class(name='CheckDisplayStereotype')
        self.assertEqual(True, pyutClass.displayStereoType)

    def testBasicPropertiesInterfaces(self):

        pyutClass: Class = Class(name='CheckInterfaces')
        self.assertTrue(len(pyutClass.interfaces) == 0, 'Where is my top level attribute`')

    def testIdIncrements(self):

        UmlModelBase.idGenerator = uniqueIdentifier()
        fakeClass: Class = Class(name='FakeClass')

        self.assertEqual('FakeClass', fakeClass.name, '')
        pyutClass1: Class = Class(name='CheckPyutObject')

        self.assertTrue(pyutClass1.id != '')
        self.assertTrue(pyutClass1.fileName == '')

        pyutClass2: Class = Class(name='BumpId')
        self.assertTrue(pyutClass2.id != pyutClass1.id)

    def testLinkedObject(self):

        pyutLinkedObject: LinkedObject = LinkedObject()

        self.assertTrue(len(pyutLinkedObject.parents) == 0, 'No parents at instantiation')
        self.assertTrue(len(pyutLinkedObject.links) == 0, 'No links at instantiation')


def suite() -> TestSuite:
    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestClass))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
