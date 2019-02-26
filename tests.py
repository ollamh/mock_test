import unittest
from unittest import mock
from io import StringIO

from .core import get_cwd, MockTester2, read_from_file

class MockTestCase(unittest.TestCase):

    def test_patch_import(self):
        with mock.patch('mock_test.core.os.getcwd', return_value='Space') as m:
            self.assertEqual(get_cwd(), 'Space')

    @mock.patch('mock_test.core.os.getcwd', return_value='Space2')
    def test_patch_decorator(self, mocked_method):
        self.assertEqual(get_cwd(), 'Space2')
        mocked_method.assert_called_once()

    def test_patch_class(self):
        with mock.patch('mock_test.core.MockTester1') as MockTester1:
            MockTester1.return_value.get_data_from_url.return_value = [1,2,3]
            tester = MockTester2()
            # Here we assert that the class was initialized with right values
            self.assertEqual(MockTester1.call_args, mock.call('AAA'))
            # Try to run tester method with controlled input, so that we know what is the output
            result = tester.process_data()
            self.assertEqual(result, 6)
            

class AutospecTestCase(unittest.TestCase):

    def test_no_autospec_bug_pass(self):
        with mock.patch('mock_test.core.MockTester1') as MockTester1:
            MockTester1.return_value.get_data_from_url.return_value = [1,2,3]
            tester = MockTester2()
            # bug (will pass, but why?)
            MockTester1.ass_called_once()

    @unittest.expectedFailure
    def test_autospec_bug_fail(self):
        with mock.patch('mock_test.core.MockTester1', autospec=True) as MockTester1:
            MockTester1.return_value.get_data_from_url.return_value = [1,2,3]
            tester = MockTester2()
            # bug will raise
            # with self.assertRaises(AttributeError):
            MockTester1.ass_called_once()


class PartialTestCase(unittest.TestCase):

    def test_patch_object(self):
        with mock.patch.object(MockTester2, 'process_data', return_value='XXX'):
            tester = MockTester2()
            self.assertEqual(tester.process_data(), 'XXX')
            self.assertNotIn('MagicMock', tester.some())



class PatchContextManagerTestCase(unittest.TestCase):

    def test_patch(self):
        with mock.patch('mock_test.core.open') as mocked_open:
            mocked_open.return_value.__enter__.return_value = StringIO('contents')
            results = read_from_file('AAA')
            self.assertEqual(results, 'contents')

