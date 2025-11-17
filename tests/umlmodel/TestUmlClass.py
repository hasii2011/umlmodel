
from unittest import TestSuite
from unittest import main as unitTestMain

from tests.ProjectTestBase import ProjectTestBase

from umlmodel.UmlClass import UmlClass
from umlmodel.UmlLinkedObject import UmlLinkedObject
from umlmodel.UmlObject import UmlObject
from umlmodel.UmlObject import uniqueIdentifier

from umlmodel.enumerations.UmlDisplayParameters import UmlDisplayParameters
from umlmodel.enumerations.UmlStereotype import UmlStereotype


class TestUmlClass(ProjectTestBase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def testMultipleInheritance(self):

        pyutClass: UmlClass = UmlClass(name='')
        self.logger.info(f'{len(pyutClass.fields)=}')

    def testLinksAndParent(self):

        pyutClass: UmlClass = UmlClass(name='CheckLinks')
        self.assertTrue(len(pyutClass.parents) == 0, 'No parents at instantiation')
        self.assertTrue(len(pyutClass.links) == 0, 'No links at instantiation')

    def testBasicPropertiesDisplayParameters(self):

        pyutClass: UmlClass = UmlClass(name='CheckDisplayProperties')
        self.assertEqual(UmlDisplayParameters.UNSPECIFIED, pyutClass.displayParameters)

    def testBasicPropertiesStereotype(self):

        pyutClass: UmlClass = UmlClass(name='CheckStereotype')
        self.assertEqual(UmlStereotype.NO_STEREOTYPE, pyutClass.stereotype)

    def testBasicPropertiesDisplayStereotype(self):

        pyutClass: UmlClass = UmlClass(name='CheckDisplayStereotype')
        self.assertEqual(True, pyutClass.displayStereoType)

    def testBasicPropertiesInterfaces(self):

        pyutClass: UmlClass = UmlClass(name='CheckInterfaces')
        self.assertTrue(len(pyutClass.interfaces) == 0, 'Where is my top level attribute`')

    def testIdIncrements(self):

        UmlObject.idGenerator = uniqueIdentifier()
        fakeClass: UmlClass = UmlClass(name='FakeClass')

        self.assertEqual('FakeClass', fakeClass.name, '')
        pyutClass1: UmlClass = UmlClass(name='CheckPyutObject')

        self.assertTrue(pyutClass1.id != '')
        self.assertTrue(pyutClass1.fileName == '')

        pyutClass2: UmlClass = UmlClass(name='BumpId')
        self.assertTrue(pyutClass2.id != pyutClass1.id)

    def testLinkedObject(self):

        pyutLinkedObject: UmlLinkedObject = UmlLinkedObject()

        self.assertTrue(len(pyutLinkedObject.parents) == 0, 'No parents at instantiation')
        self.assertTrue(len(pyutLinkedObject.links) == 0, 'No links at instantiation')



def suite() -> TestSuite:
    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestUmlClass))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
