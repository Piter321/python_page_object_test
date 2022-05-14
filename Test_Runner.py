from unittest import TestLoader, TestSuite, TextTestRunner
from test import Google_HomePage
from test2 import Google_Search
import testtools as testtools

if __name__ == "__main__":
    test_loader = TestLoader()
    # Test Suite is used since there are multiple test cases
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(Google_HomePage),
        test_loader.loadTestsFromTestCase(Google_Search),
    ))

    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)

    # Refer https://testtools.readthedocs.io/en/latest/api.html for more information
    parallel_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in test_suite))
    parallel_suite.run(testtools.StreamResult())
        # self.driver.set_page_load_timeout(30))